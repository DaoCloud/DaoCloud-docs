<?php
namespace Grav\Plugin\Login;

use Grav\Common\Grav;
use Grav\Common\User\User;
use Grav\Common\File\CompiledYamlFile;
use Grav\Common\Utils;
use Grav\Plugin\Login\Utils as LoginUtils;

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
            $this->setMessage($t->translate('PLUGIN_LOGIN.LOGIN_SUCCESSFUL'));
            $referrer = $this->grav['uri']->referrer('/');
            $this->setRedirect($referrer);
        } else {
            $user = $this->grav['user'];
            if ($user->username) {
                $this->setMessage($t->translate('PLUGIN_LOGIN.ACCESS_DENIED'));
            } else {
                $this->setMessage($t->translate('PLUGIN_LOGIN.LOGIN_FAILED'));
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
     * Handle the email password recovery procedure.
     *
     * @return bool True if the action was performed.
     */
    protected function taskForgot()
    {
        $param_sep = $this->grav['config']->get('system.param_sep', ':');
        $data = $this->post;

        $username = isset($data['username']) ? $data['username'] : '';
        $user = !empty($username) ? User::load($username) : null;

        /** @var Language $l */
        $language = $this->grav['language'];
        $messages = $this->grav['messages'];

        if (!isset($this->grav['Email'])) {
            $messages->add($language->translate('PLUGIN_ADMIN.FORGOT_EMAIL_NOT_CONFIGURED'), 'error');
            $this->setRedirect('/');
            return true;
        }

        if (!$user || !$user->exists()) {
            $messages->add($language->translate(['PLUGIN_ADMIN.FORGOT_USERNAME_DOES_NOT_EXIST', $username]), 'error');
            $this->setRedirect('/forgot');
            return true;
        }

        if (empty($user->email)) {
            $messages->add($language->translate(['PLUGIN_ADMIN.FORGOT_CANNOT_RESET_EMAIL_NO_EMAIL', $username]), 'error');
            $this->setRedirect('/forgot');
            return true;
        }

        $token = md5(uniqid(mt_rand(), true));
        $expire = time() + 604800; // next week

        $user->reset = $token . '::' . $expire;
        $user->save();

        $author = $this->grav['config']->get('site.author.name', '');
        $fullname = $user->fullname ?: $username;

        $reset_link = $this->grav['base_url_absolute'] . $this->grav['config']->get('plugins.login.route_reset') . '/task:login.reset/token' . $param_sep . $token . '/user' . $param_sep . $username . '/nonce' . $param_sep . Utils::getNonce('reset-form');

        $sitename = $this->grav['config']->get('site.title', 'Website');
        $from = $this->grav['config']->get('plugins.email.from');

        if (empty($from)) {
            $messages->add($language->translate('PLUGIN_ADMIN.FORGOT_EMAIL_NOT_CONFIGURED'), 'error');
            $this->setRedirect('/forgot');
            return true;
        }

        $to = $user->email;

        $subject = $language->translate(['PLUGIN_ADMIN.FORGOT_EMAIL_SUBJECT', $sitename]);
        $content = $language->translate(['PLUGIN_ADMIN.FORGOT_EMAIL_BODY', $fullname, $reset_link, $author, $sitename]);

        $sent = LoginUtils::sendEmail($subject, $content, $to);

        if ($sent < 1) {
            $messages->add($language->translate('PLUGIN_ADMIN.FORGOT_FAILED_TO_EMAIL'), 'error');
        } else {
            $messages->add($language->translate(['PLUGIN_ADMIN.FORGOT_INSTRUCTIONS_SENT_VIA_EMAIL', $to]), 'info');
        }

        $this->setRedirect('/');
        return true;
    }

    /**
     * Handle the reset password action.
     *
     * @return bool True if the action was performed.
     */
    public function taskReset()
    {
        $data = $this->post;
        $language = $this->grav['language'];
        $messages = $this->grav['messages'];

        if (isset($data['password'])) {
            $username = isset($data['username']) ? $data['username'] : null;
            $user = !empty($username) ? User::load($username) : null;
            $password = isset($data['password']) ? $data['password'] : null;
            $token = isset($data['token']) ? $data['token'] : null;

            if (!empty($user) && $user->exists() && !empty($user->reset)) {
                list($good_token, $expire) = explode('::', $user->reset);

                if ($good_token === $token) {
                    if (time() > $expire) {
                        $messages->add($language->translate('PLUGIN_ADMIN.RESET_LINK_EXPIRED'), 'error');
                        $this->grav->redirect($this->grav['config']->get('plugins.login.route_forgot'));
                        return true;
                    }

                    unset($user->hashed_password);
                    unset($user->reset);
                    $user->password = $password;

                    $user->validate();
                    $user->filter();
                    $user->save();

                    $messages->add($language->translate('PLUGIN_ADMIN.RESET_PASSWORD_RESET'), 'info');
                    $this->grav->redirect('/');
                    return true;
                }
            }

            $messages->add($language->translate('PLUGIN_ADMIN.RESET_INVALID_LINK'), 'error');
            $this->grav->redirect($this->grav['config']->get('plugins.login.route_forgot'));
            return true;

        } else {
            $user = $this->grav['uri']->param('user');
            $token = $this->grav['uri']->param('token');

            if (empty($user) || empty($token)) {
                $messages->add($language->translate('PLUGIN_ADMIN.RESET_INVALID_LINK'), 'error');
                $this->grav->redirect($this->grav['config']->get('plugins.login.route_forgot'));
                return true;
            }
        }

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
