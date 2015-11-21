<?php
namespace Grav\Plugin\Login;

use Grav\Common\Grav;
use Grav\Common\User\User;
use Grav\Common\File\CompiledYamlFile;

use RocketTheme\Toolbox\Session\Message;

class LoginController extends Controller
{
    /**
     * @var string
     */
    protected $prefix = 'task';

    /**
     * Handle login.
     *
     * @return bool True if the action was performed.
     */
    public function taskLogin()
    {
        $t = $this->grav['language'];
        if ($this->authenticate($this->post)) {
            $this->setMessage($t->translate('LOGIN_PLUGIN.LOGIN_SUCCESSFUL'));
            $referrer = $this->grav['uri']->referrer('/');
            $this->setRedirect($referrer);
        } else {
            $user = $this->grav['user'];
            if ($user->username) {
                $this->setMessage($t->translate('LOGIN_PLUGIN.ACCESS_DENIED'));
            } else {
                $this->setMessage($t->translate('LOGIN_PLUGIN.LOGIN_FAILED'));
            }
        }

        return true;
    }

    /**
     * Handle logout.
     *
     * @return bool True if the action was performed.
     */
    public function taskLogout()
    {
        /** @var User $user */
        $user = $this->grav['user'];

        if (!$this->rememberMe->login()) {
            $credentials = $user->get('username');
            $this->rememberMe->getStorage()->cleanAllTriplets($credentials);
        }
        $this->rememberMe->clearCookie();

        $this->grav['session']->invalidate()->start();
        $this->setRedirect('/');

        return true;
    }

    /**
     * Authenticate user.
     *
     * @param  array $form Form fields.
     * @return bool
     */
    protected function authenticate($form)
    {
        /** @var User $user */
        $user = $this->grav['user'];

        if (!$user->authenticated) {
            $username = isset($form['username']) ? $form['username'] : $this->rememberMe->login();

            // Normal login process
            $user = User::load($username);
            if ($user->exists()) {
                if (!empty($form['username']) && !empty($form['password'])) {
                    // Authenticate user.
                    $result = $user->authenticate($form['password']);

                    if ($result) {
                        $this->grav['session']->user = $user;

                        unset($this->grav['user']);
                        $this->grav['user'] = $user;

                        // If the user wants to be remembered, create
                        // Rememberme cookie
                        if (!empty($form['rememberme'])) {
                            $this->rememberMe->createCookie($form['username']);
                        } else {
                            $this->rememberMe->clearCookie();
                            $this->rememberMe->getStorage()->cleanAllTriplets($user->get('username'));
                        }
                    }
                }
            }
        }

        // Authorize against user ACL
        $user->authenticated = $user->authorize('site.login');
        return $user->authenticated;
    }
}
