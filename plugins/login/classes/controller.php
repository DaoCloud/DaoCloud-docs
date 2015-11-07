<?php
namespace Grav\Plugin;

use Grav\Common\File\CompiledYamlFile;
use Grav\Common\Grav;
use Grav\Common\User\User;
use RocketTheme\Toolbox\Session\Message;

class LoginController
{
    /**
     * @var Grav
     */
    public $grav;

    /**
     * @var string
     */
    public $view;

    /**
     * @var string
     */
    public $task;

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
     * @param Grav   $grav
     * @param string $task
     * @param array  $post
     */
    public function __construct(Grav $grav, $task, $post)
    {
        $this->grav = $grav;
        $this->task = $task ?: 'display';
        $this->post = $this->getPost($post);
    }

    /**
     * Performs a task.
     */
    public function execute()
    {
        // Set redirect if available.
        if (isset($this->post['_redirect'])) {
            $redirect = $this->post['_redirect'];
            unset($this->post['_redirect']);
        }

        $success = false;
        $method = 'task' . ucfirst($this->task);

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

    public function redirect()
    {
        if ($this->redirect) {
            $this->grav->redirect($this->redirect, $this->redirectCode);
        }
    }

    /**
     * Handle login.
     *
     * @return bool True if the action was performed.
     */
    public function taskLogin()
    {
        $t = $this->grav['language'];
        $user = $this->grav['user'];

        if ($this->authenticate($this->post)) {
            $this->setMessage($t->translate('LOGIN_PLUGIN.LOGIN_SUCCESSFUL'));
            $referrer = $this->grav['uri']->referrer('/');
            $this->setRedirect($referrer);
        } else {
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

        if (!$user->authenticated && isset($form['username']) && isset($form['password'])) {
            $user = User::load($form['username']);
            if ($user->exists()) {

                // Authenticate user.
                $result = $user->authenticate($form['password']);

                if ($result) {
                    $this->grav['session']->user = $user;
                }
            }
        }
        $user->authenticated = $user->authorize('site.login');

        return $user->authenticated;
    }

    /**
     * Set redirect.
     *
     * @param $path
     * @param int $code
     */
    public function setRedirect($path, $code = 303)
    {
        $this->redirect = '/' . preg_replace('|/+|', '/', trim($path, '/'));
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
     * Prepare and return POST data.
     *
     * @param array $post
     * @return array
     */
    protected function &getPost($post)
    {
        unset($post['task']);

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
