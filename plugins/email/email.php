<?php
namespace Grav\Plugin;

use Grav\Common\Plugin;
use Grav\Common\Twig\Twig;
use RocketTheme\Toolbox\Event\Event;

class EmailPlugin extends Plugin
{
    /**
     * @var Email
     */
    protected $email;

    /**
     * @return array
     */
    public static function getSubscribedEvents()
    {
        return [
            'onPluginsInitialized' => ['onPluginsInitialized', 0],
            'onFormProcessed' => ['onFormProcessed', 0]
        ];
    }

    /**
     * Initialize emailing.
     */
    public function onPluginsInitialized()
    {
        require_once __DIR__ . '/classes/email.php';
        require_once __DIR__ . '/vendor/autoload.php';

        $this->email = new Email();

        if ($this->email->enabled()) {
            $this->grav['Email'] = $this->email;
        }
    }

    /**
     * Send email when processing the form data.
     *
     * @param Event $event
     */
    public function onFormProcessed(Event $event)
    {
        $form = $event['form'];
        $action = $event['action'];
        $params = $event['params'];

        if (!$this->email->enabled()) {
            return;
        }

        switch ($action) {
            case 'email':
                // Prepare Twig variables
                $vars = array(
                    'form' => $form
                );

                // Build message
                $message = $this->buildMessage($params, $vars);

                // Send e-mail
                $this->email->send($message);
                break;
        }
    }

    /**
     * Build e-mail message.
     *
     * @param array $params
     * @param array $vars
     * @return \Swift_Message
     */
    protected function buildMessage(array $params, array $vars = array())
    {
        /** @var Twig $twig */
        $twig = $this->grav['twig'];

        // Extend parameters with defaults.
        $params += array(
            'bcc' => array(),
            'body' => '{% include "forms/data.html.twig" %}',
            'cc' => array(),
            'charset' => 'utf-8',
            'from' => $this->config->get('plugins.email.from'),
            'from_name' => $this->config->get('plugins.email.from_name'),
            'content_type' => $this->config->get('plugins.email.content_type', 'text/html'),
            'reply_to' => array(),
            'subject' => !empty($vars['form']) && $vars['form'] instanceof Form ? $vars['form']->page()->title() : null,
            'to' => $this->config->get('plugins.email.to'),
            'to_name' => $this->config->get('plugins.email.to_name'),
        );

        // Create message object.
        $message = $this->email->message();

        // Process parameters.
        foreach ($params as $key => $value) {
            switch ($key) {
                case 'bcc':
                    foreach ($this->parseAddressValue($value, $vars) as $address) {
                        $message->addBcc($address->mail, $address->name);
                    }
                    break;

                case 'body':
                    if (is_string($value)) {
                        $body = $twig->processString($value, $vars);
                        $content_type = !empty($params['content_type']) ? $twig->processString($params['content_type'], $vars) : null;
                        $charset = !empty($params['charset']) ? $twig->processString($params['charset'], $vars) : null;

                        $message->setBody($body, $content_type, $charset);
                    }
                    elseif (is_array($value)) {
                        foreach ($value as $body_part) {
                            $body = !empty($body_part['body']) ? $twig->processString($body_part['body'], $vars) : null;
                            $content_type = !empty($body_part['content_type']) ? $twig->processString($body_part['content_type'], $vars) : null;
                            $charset = !empty($body_part['charset']) ? $twig->processString($body_part['charset'], $vars) : null;

                            if (!$message->getBody()) {
                                $message->setBody($body, $content_type, $charset);
                            }
                            else {
                                $message->addPart($body, $content_type, $charset);
                            }
                        }
                    }
                    break;

                case 'cc':
                    foreach ($this->parseAddressValue($value, $vars) as $address) {
                        $message->addCc($address->mail, $address->name);
                    }
                    break;

                case 'from':
                    if (is_string($value) && !empty($params['from_name'])) {
                        $value = array(
                            'mail' => $twig->processString($value, $vars),
                            'name' => $twig->processString($params['from_name'], $vars),
                        );
                    }

                    foreach ($this->parseAddressValue($value, $vars) as $address) {
                        $message->addFrom($address->mail, $address->name);
                    }
                    break;

                case 'reply_to':
                    foreach ($this->parseAddressValue($value, $vars) as $address) {
                        $message->addReplyTo($address->mail, $address->name);
                    }
                    break;

                case 'subject':
                    $message->setSubject($twig->processString($value, $vars));
                    break;

                case 'to':
                    if (is_string($value) && !empty($params['to_name'])) {
                        $value = array(
                          'mail' => $twig->processString($value, $vars),
                          'name' => $twig->processString($params['to_name'], $vars),
                        );
                    }

                    foreach ($this->parseAddressValue($value, $vars) as $address) {
                        $message->addTo($address->mail, $address->name);
                    }
                    break;
            }
        }

        return $message;
    }

    /**
     * Return parsed e-mail address value.
     *
     * @param $value
     * @param array $vars
     * @return array
     */
    protected function parseAddressValue($value, array $vars = array())
    {
        $parsed = array();

        /** @var Twig $twig */
        $twig = $this->grav['twig'];

        // Single e-mail address string
        if (is_string($value)) {
            $parsed[] = (object) array(
                'mail' => $twig->processString($value, $vars),
                'name' => null,
            );
        }

        else {
            // Cast value as array
            $value = (array) $value;

            // Single e-mail address array
            if (!empty($value['mail'])) {
                $parsed[] = (object) array(
                  'mail' => $twig->processString($value['mail'], $vars),
                  'name' => !empty($value['name']) ? $twig->processString($value['name'], $vars) : NULL,
                );
            }

            // Multiple addresses (either as strings or arrays)
            elseif (!(empty($value['mail']) && !empty($value['name']))) {
                foreach ($value as $y => $itemx) {
                    $addresses = $this->parseAddressValue($itemx, $vars);

                    if (($address = reset($addresses))) {
                        $parsed[] = $address;
                    }
                }
            }
        }

        return $parsed;
    }
}
