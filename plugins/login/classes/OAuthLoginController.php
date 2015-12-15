<?php

namespace Grav\Plugin\Login;

use Grav\Common\Grav;
use Grav\Common\Inflector;
use Grav\Common\User\User;
use Grav\Common\File\CompiledYamlFile;

use OAuth\ServiceFactory;
use OAuth\Common\Storage\Session;
use OAuth\Common\Consumer\Credentials;
use OAuth\Common\Http\Client\CurlClient;

/**
 * OAuthLoginController
 *
 * Handles OAuth authentication.
 *
 * @author  Sommerregen <sommerregen@benjamin-regler.de>
 */
class OAuthLoginController extends Controller
{
    /**
     * @var string
     */
    public $provider;

    /**
     * @var \OAuth\Common\Storage\Session
     */
    protected $storage;

    /**
     * @var \OAuth\ServiceFactory
     */
    protected $factory;

    /**
     * @var \OAuth\Common\Service\AbstractService
     */
    protected $service;

    /**
     * @var string
     */
    protected $prefix = 'oauth';

    /**
     * @var array
     */
    protected $scopes = [
        'github' => ['user'],
        'google' => ['userinfo_email', 'userinfo_profile'],
        'facebook' => ['public_profile']
    ];

    /**
     * Constructor.
     *
     * @param Grav   $grav   Grav instance
     * @param string $action The name of the action
     * @param array  $post   An array of values passed to the action
     */
    public function __construct(Grav $grav, $action, $post = null)
    {
        parent::__construct($grav, ucfirst($action), $post);

        // Session storage
        $this->storage = new Session(false, 'oauth_token', 'oauth_state');

        /** @var $serviceFactory \OAuth\ServiceFactory */
        $this->factory = new ServiceFactory();

        // Use curl client instead of fopen stream
        if (extension_loaded('curl')) {
            $this->factory->setHttpClient(new CurlCLient());
        }
    }

    /**
     * Performs an OAuth authentication
     */
    public function execute()
    {
        /** @var \Grav\Common\Language\Language */
        $t = $this->grav['language'];

        $provider = strtolower($this->action);
        $config = $this->grav['config']->get('plugins.login.oauth.providers.' . $this->action, []);

        if (isset($config['credentials'])) {
            // Setup the credentials for the requests
            $credentials = new Credentials(
                $config['credentials']['key'], $config['credentials']['secret'], $this->grav['uri']->url(true)
            );

            // Instantiate service using the credentials, http client
            // and storage mechanism for the token
            $scope = isset($this->scopes[$provider]) ? $this->scopes[$provider] : [];
            $this->service = $this->factory->createService($this->action, $credentials, $this->storage, $scope);
        }

        if (!$this->service || empty($config)) {
            $this->setMessage($t->translate(['PLUGIN_LOGIN.OAUTH_PROVIDER_NOT_SUPPORTED', $this->action]));
            return true;
        }

        // Check OAuth authentication status
        $authenticated = parent::execute();
        if (is_bool($authenticated)) {
            $this->reset();
            if ($authenticated) {
                $this->setMessage($t->translate('PLUGIN_LOGIN.LOGIN_SUCCESSFUL'));
            } else {
                $this->setMessage($t->translate('PLUGIN_LOGIN.ACCESS_DENIED'));
            }

            // Redirect to current URI
            $referrer = $this->grav['uri']->url(true);
            $this->setRedirect($referrer);
        } elseif (!$this->grav['session']->oauth) {
            $this->setMessage($t->translate(['PLUGIN_LOGIN.OAUTH_PROVIDER_NOT_SUPPORTED', $this->action]));
        }

        return true;
    }

    /**
     * Reset state of OAuth authentication.
     */
    public function reset() {
        /** @var Grav\Common\Session */
        $session = $this->grav['session'];

        unset($session->oauth);
        $this->storage->clearAllTokens();
        $this->storage->clearAllAuthorizationStates();
    }

    /**
     * Implements a generic OAuth service provider authentication
     *
     * @param  callable $callback A callable to call when OAuth authentication
     *                            starts
     * @param  string   $oauth    OAuth version to be used for authentication
     *
     * @return null|User          Returns a Grav user instance on success.
     */
    protected function genericOAuthProvider($callback, $oauth = 'oauth2')
    {
        /** @var Grav\Common\Session */
        $session = $this->grav['session'];

        switch ($oauth) {
            case 'oauth1':
                if (empty($_GET['oauth_token']) && empty($_GET['oauth_verifier'])) {
                    // Extra request needed for OAuth1 to request a request token :-)
                    $token = $this->service->requestRequestToken();

                    // Create a state token to prevent request forgery.
                    // Store it in the session for later validation.
                    $redirect = $this->service->getAuthorizationUri([
                        'oauth_token' => $token->getRequestToken()
                    ]);
                    $this->setRedirect($redirect);

                    // Update OAuth session
                    $session->oauth = $this->action;
                } else {
                    $token = $this->storage->retrieveAccessToken($session->oauth);

                    // This was a callback request from OAuth1 service, get the token
                    $this->service->requestAccessToken(
                        $_GET['oauth_token'],
                        $_GET['oauth_verifier'],
                        $token->getRequestTokenSecret()
                    );

                    return $callback();
                }
                break;

            case 'oauth2':
            default:
                if (empty($_GET['code'])) {
                    // Create a state token to prevent request forgery (CSRF).
                    $state = sha1($this->getRandomBytes(1024, false));
                    $redirect = $this->service->getAuthorizationUri([
                        'state' => $state
                    ]);
                    $this->setRedirect($redirect);

                    // Update OAuth session
                    $session->oauth = $this->action;

                    // Store CSRF in the session for later validation.
                    $this->storage->storeAuthorizationState($this->action, $state);
                } else {
                    // Retrieve the CSRF state parameter
                    $state = isset($_GET['state']) ? $_GET['state'] : null;

                    // This was a callback request from the OAuth2 service, get the token
                    $this->service->requestAccessToken($_GET['code'], $state);

                    return $callback();
                }
                break;
        }
    }

    /**
     * Implements OAuth authentication for Facebook
     *
     * @return null|bool          Returns a boolean on finished authentication.
     */
    public function oauthFacebook()
    {
        return $this->genericOAuthProvider(function() {
            // Send a request now that we have access token
            $data = json_decode($this->service->request('/me'), true);
            $email = isset($data['email']) ? $data['email'] : '';

            // Authenticate OAuth user against Grav system.
            return $this->authenticate($data['name'], $data['id'], $email);
        });
    }

    /**
     * Implements OAuth authentication for Google
     *
     * @return null|bool          Returns a boolean on finished authentication.
     */
    public function oauthGoogle()
    {
        return $this->genericOAuthProvider(function() {
            // Get username, email and language
            $data = json_decode($this->service->request('userinfo'), true);

            $username = $data['given_name'] . ' ' . $data['family_name'];
            if (preg_match('~[\w\s]+\((\w+)\)~i', $data['name'], $matches)) {
                $username = $matches[1];
            }
            $lang = isset($data['lang']) ? $data['lang'] : '';

            // Authenticate OAuth user against Grav system.
            return $this->authenticate($username, $data['id'], $data['email'], $lang);
        });
    }

    /**
     * Implements OAuth authentication for GitHub
     *
     * @return null|bool          Returns a boolean on finished authentication.
     */
    public function oauthGithub()
    {
        return $this->genericOAuthProvider(function() {
            // Get username, email and language
            $user = json_decode($this->service->request('user'), true);
            $emails = json_decode($this->service->request('user/emails'), true);

            // Authenticate OAuth user against Grav system.
            return $this->authenticate($user['login'], $user['id'], reset($emails));
        });
    }

    /**
     * Implements OAuth authentication for Twitter
     *
     * @return null|bool          Returns a boolean on finished authentication.
     */
    public function oauthTwitter()
    {
        return $this->genericOAuthProvider(function() {
            // Get username, email and language
            $data = json_decode(
                $this->service->request('account/verify_credentials.json?include_email=true'),
            true);
            $lang = isset($data['lang']) ? $data['lang'] : '';

            // Authenticate OAuth user against Grav system.
            return $this->authenticate($data['screen_name'], $data['id'], '', $lang);
        }, 'oauth1');
    }

    /**
     * Authenticate user.
     *
     * @param  string $username The username of the OAuth user
     * @param  string $email    The email of the OAuth user
     * @param  string $language Language
     *
     * @return bool             True if user was authenticated
     */
    protected function authenticate($username, $id, $email, $language = '')
    {
        $accountFile = $this->grav['inflector']->underscorize($username);
        $user = User::load(strtolower("$accountFile.{$this->action}"));

        if ($user->exists()) {
            // Update username (hide OAuth from user)
            $user->set('username', $username);

            $password = md5($id);
            $authenticated = $user->authenticate($password);
        } else {
            /** @var User $user */
            $user = $this->grav['user'];

            // Check user rights
            if (!$user->authenticated) {
                $oauthUser = $this->grav['config']->get('plugins.login.oauth.user', []);

                // Create new user from OAuth request
                $user = $this->createUser([
                    'id' => $id,
                    'username' => $username,
                    'email' => $email,
                    'lang' => $language,
                    'access' => $oauthUser['access']
                ], $oauthUser['autocreate']);
            }

            // Authenticate user against oAuth rules
            $authenticated = $user->authenticated;
        }

        // Store user in session
        if ($authenticated) {
            $this->grav['session']->user = $user;

            unset($this->grav['user']);
            $this->grav['user'] = $user;
        }

        return $authenticated;
    }

    /**
     * Create user.
     *
     * @param  string $data['username']   The username of the OAuth user
     * @param  string $data['password']   The unique id of the Oauth user
     *                                    setting as password
     * @param  string $data['email']      The email of the OAuth user
     * @param  string $data['language']   Language
     * @param  bool   $save               Save user
     *
     * @return User                       A user object
     */
    protected function createUser($data, $save = false)
    {
        /** @var User $user */
        $user = $this->grav['user'];

        $accountFile = $this->grav['inflector']->underscorize($data['username']);
        $accountFile = $this->grav['locator']->findResource('user://accounts/' . strtolower("$accountFile.{$this->action}") . YAML_EXT, true, true);

        $user->set('username', $data['username']);
        $user->set('password', md5($data['id']));
        $user->set('email', $data['email']);
        $user->set('lang', $data['lang']);

        // Set access rights
        $user->join('access',
            $this->grav['config']->get('plugins.login.oauth.user.access', [])
        );

        // Authorize OAuth user to access page(s)
        $user->authenticated = $user->authorize('site.login');

        if ($save) {
            $user->file(CompiledYamlFile::instance($accountFile));
            $user->save();
        }

        return $user;
    }

     /**
      * Generates Random Bytes for the given $length.
      *
      * @param  int     $length The number of bytes to generate
      * @param  bool    $secure Return cryptographic secure string or not
      *
      * @return string
      *
      * @throws InvalidArgumentException when an invalid length is specified.
      * @throws RuntimeException when no secure way of making bytes is posible
      */
    protected function getRandomBytes($length = 0, $secure = true)
    {
        if ($length < 1) {
            throw new \InvalidArgumentException('The length parameter must be a number greater than zero!');
        }

        /**
         * Our primary choice for a cryptographic strong randomness function is
         * openssl_random_pseudo_bytes.
         */
        if (function_exists('openssl_random_pseudo_bytes')) {
            $bytes = openssl_random_pseudo_bytes($length, $sec);
            if ($sec === true) {
                return $bytes;
            }
        }

        /**
         * If mcrypt extension is available then we use it to gather entropy from
         * the operating system's PRNG. This is better than reading /dev/urandom
         * directly since it avoids reading larger blocks of data than needed.
         * Older versions of mcrypt_create_iv may be broken or take too much time
         * to finish so we only use this function with PHP 5.3.7 and above.
         * @see https://bugs.php.net/bug.php?id=55169
         */
        if (function_exists('mcrypt_create_iv') &&
            (strtolower(substr(PHP_OS, 0, 3)) !== 'win' ||
            version_compare(PHP_VERSION, '5.3.7') >= 0)) {
            $bytes = mcrypt_create_iv($length, MCRYPT_DEV_URANDOM);
            if ($bytes !== false) {
                return $bytes;
            }
        }

        if ($secure) {
            throw new \RuntimeException('There is no possible way of making secure bytes');
        }

        /**
         * Fallback (not really secure, but better than nothing)
         */
        return hex2bin(substr(str_shuffle(str_repeat('0123456789abcdef', $length*16)), 0, $length));
    }
}
