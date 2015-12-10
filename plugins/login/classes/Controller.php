<?php

namespace Grav\Plugin\Login;

use Grav\Common\Grav;
use Grav\Common\Utils;
use Grav\Plugin\Login\RememberMe;

use Birke\Rememberme\Cookie;

class Controller implements ControllerInterface
{
    /**
     * @var \Grav\Common\Grav
     */
    public $grav;

    /**
     * @var string
     */
    public $action;

    /**
     * @var array
     */
    public $post;

    /**
     * @var string
     */
    protected $redirect;

    /**
     * @var int
     */
    protected $redirectCode;

    /**
     * @var string
     */
    protected $prefix = 'do';

    /**
     * @var \Birke\Rememberme\Authenticator
     */
    protected $rememberMe;

    /**
     * @param Grav   $grav
     * @param string $action
     * @param array  $post
     */
    public function __construct(Grav $grav, $action, $post = null)
    {
        $this->grav = $grav;
        $this->action = $action;
        $this->post = $this->getPost($post);

        $this->rememberMe();
    }

    /**
     * Performs an action.
     */
    public function execute()
    {
        // Set redirect if available.
        if (isset($this->post['_redirect'])) {
            $redirect = $this->post['_redirect'];
            unset($this->post['_redirect']);
        }

        $success = false;
        $method = $this->prefix . ucfirst($this->action);

        if (!method_exists($this, $method)) {
            throw new \RuntimeException('Page Not Found', 404);
        }

        try {
            $success = call_user_func(array($this, $method));
        } catch (\RuntimeException $e) {
            $this->setMessage($e->getMessage());
        }

        if (!$this->redirect && isset($redirect)) {
            $this->setRedirect($redirect);
        }

        return $success;
    }

    /**
     * Redirects an action
     */
    public function redirect()
    {
        $redirect = $this->grav['config']->get('plugins.login.redirect');
        if ($redirect) {
            $this->grav->redirect($redirect, $this->redirectCode);
        } else if ($this->redirect) {
            $this->grav->redirect($this->redirect, $this->redirectCode);
        }
    }

    /**
     * Set redirect.
     *
     * @param $path
     * @param int $code
     */
    public function setRedirect($path, $code = 303)
    {
        $this->redirect = $path;
        $this->code = $code;
    }

    /**
     * Add message into the session queue.
     *
     * @param string $msg
     * @param string $type
     */
    public function setMessage($msg, $type = 'info')
    {
        /** @var Message $messages */
        $messages = $this->grav['messages'];
        $messages->add($msg, $type);
    }

    /**
     * Gets and sets the RememberMe class
     *
     * @param  mixed            $var    A rememberMe instance to set
     *
     * @return Authenticator            Returns the current rememberMe instance
     */
    public function rememberMe($var = null)
    {
        if ($var !== null) {
            $this->rememberMe = $var;
        }
        if (!$this->rememberMe) {
            /** @var Config $config */
            $config = $this->grav['config'];

            // Setup storage for RememberMe cookies
            $storage = new RememberMe\TokenStorage();
            $this->rememberMe = new RememberMe\RememberMe($storage);
            $this->rememberMe->setCookieName($config->get('plugins.login.rememberme.name'));
            $this->rememberMe->setExpireTime($config->get('plugins.login.rememberme.timeout'));

            // Hardening cookies with user-agent and random salt or
            // fallback to use system based cache key
            $data = $_SERVER['HTTP_USER_AGENT'] . $config->get('security.salt', $this->grav['cache']->getKey());
            $this->rememberMe->setSalt(hash('sha512', $data));

            // Set cookie with correct base path of Grav install
            $cookie = new Cookie();
            $cookie->setPath($this->grav['base_url_relative']);
            $this->rememberMe->setCookie($cookie);
        }

        return $this->rememberMe;
    }

    /**
     * Prepare and return POST data.
     *
     * @param array $post
     * @return array
     */
    protected function &getPost($post)
    {
        unset($post[$this->prefix]);

        // Decode JSON encoded fields and merge them to data.
        if (isset($post['_json'])) {
            $post = array_merge_recursive($post, $this->jsonDecode($post['_json']));
            unset($post['_json']);
        }
        return $post;
    }

    /**
     * Recursively JSON decode data.
     *
     * @param  array $data
     * @return array
     */
    protected function jsonDecode(array $data)
    {
        foreach ($data as &$value) {
            if (is_array($value)) {
                $value = $this->jsonDecode($value);
            } else {
                $value = json_decode($value, true);
            }
        }
        return $data;
    }
}
