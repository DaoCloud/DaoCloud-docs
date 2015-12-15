<?php

namespace Grav\Plugin\Login;

use Grav\Common\Grav;

class Utils
{
    /**
     * Handle sending an email.
     *
     * @param string $content
     * @param string $to
     *
     * @return bool True if the action was performed.
     */
    public static function sendEmail($subject, $content, $to)
    {
        $grav = Grav::instance();

        $from = $grav['config']->get('plugins.email.from');

        if (!isset($grav['Email']) || empty($from)) {
            throw new \RuntimeException($grav['language']->translate('PLUGIN_LOGIN.EMAIL_NOT_CONFIGURED'));
        }

        if (empty($to) || empty($subject) || empty($content)) {
            return false;
        }

        //Initialize twig if not yet initialized
        $grav['twig']->init();

        $body = $grav['twig']->processTemplate('email/base.html.twig', ['content' => $content]);

        $message = $grav['Email']->message($subject, $body, 'text/html')
            ->setFrom($from)
            ->setTo($to);

        $sent = $grav['Email']->send($message);

        if ($sent < 1) {
            return false;
        } else {
            return true;
        }
    }
}
