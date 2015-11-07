<?php
namespace Grav\Plugin;

use Grav\Common\Config\Config;
use Grav\Common\GravTrait;

class Email
{
    use GravTrait;

    /**
     * @var \Swift_Transport
     */
    protected $mailer;

    /**
     * Returns true if emails have been enabled in the system.
     *
     * @return bool
     */
    public function enabled()
    {
        return self::getGrav()['config']->get('plugins.email.mailer.engine') != 'none';
    }

    /**
     * Creates an email message.
     *
     * @param string $subject
     * @param string $body
     * @param string $contentType
     * @param string $charset
     * @return \Swift_Message
     */
    public function message($subject = null, $body = null, $contentType = null, $charset = null)
    {
        return new \Swift_Message($subject, $body, $contentType, $charset);
    }

    /**
     * Creates an attachment.
     *
     * @param string $data
     * @param string $filename
     * @param string $contentType
     * @return \Swift_Attachment
     */
    public function attachment($data = null, $filename = null, $contentType = null)
    {
        return new \Swift_Attachment($data, $filename, $contentType);
    }

    /**
     * Creates an embedded attachment.
     *
     * @param string $data
     * @param string $filename
     * @param string $contentType
     * @return \Swift_EmbeddedFile
     */
    public function embedded($data = null, $filename = null, $contentType = null)
    {
        return new \Swift_EmbeddedFile($data, $filename, $contentType);
    }

    /**
     * Creates an image attachment.
     *
     * @param string $data
     * @param string $filename
     * @param string $contentType
     * @return \Swift_Image
     */
    public function image($data = null, $filename = null, $contentType = null)
    {
        return new \Swift_Image($data, $filename, $contentType);
    }

    /**
     * Send email.
     *
     * @param \Swift_Message $message
     * @return int
     */
    public function send($message)
    {
        $mailer = $this->getMailer();

        return $mailer ? $mailer->send($message) : 0;
    }

    /**
     * @internal
     * @return null|\Swift_Mailer
     */
    protected function getMailer()
    {
        if (!$this->enabled()) {
            return null;
        }

        if (!$this->mailer) {
            /** @var Config $config */
            $config = self::getGrav()['config'];
            $mailer = $config->get('plugins.email.mailer.default');

            // Create the Transport and initialize it.
            switch ($mailer) {
                case 'smtp':
                    $transport = \Swift_SmtpTransport::newInstance();

                    $options = $config->get('plugins.email.mailer.smtp');
                    if (!empty($options['server'])) {
                        $transport->setHost($options['server']);
                    }
                    if (!empty($options['port'])) {
                        $transport->setPort($options['port']);
                    }
                    if (!empty($options['encryption']) && $options['encryption'] != 'none') {
                        $transport->setEncryption($options['encryption']);
                    }
                    if (!empty($options['user'])) {
                        $transport->setUsername($options['user']);
                    }
                    if (!empty($options['password'])) {
                        $transport->setPassword($options['password']);
                    }
                    break;
                case 'sendmail':
                    $options = $config->get('plugins.email.mailer.sendmail');
                    $bin = !empty($options['bin']) ? $options['bin'] : '/usr/sbin/sendmail';
                    $transport = \Swift_SendmailTransport::newInstance($bin);
                    break;
                case 'mail':
                default:
                    $transport = \Swift_MailTransport::newInstance();
            }

            // Create the Mailer using your created Transport
            $this->mailer = \Swift_Mailer::newInstance($transport);
        }

        return $this->mailer;
    }
}
