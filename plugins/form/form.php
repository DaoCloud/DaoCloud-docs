<?php
namespace Grav\Plugin;

use Grav\Common\Plugin;
use Grav\Common\Page\Page;
use Grav\Common\Page\Pages;
use Grav\Common\Grav;
use Grav\Common\Uri;
use Grav\Common\Twig;
use Grav\Plugin\Form;
use RocketTheme\Toolbox\Event\Event;
use RocketTheme\Toolbox\File\File;
use Symfony\Component\Yaml\Yaml;

class FormPlugin extends Plugin
{

    /**
     * @var bool
     */
    protected $active = false;

    /**
     * @var Form
     */
    protected $form;

    /**
     * @return array
     */
    public static function getSubscribedEvents()
    {
        return [
            'onPageInitialized' => ['onPageInitialized', 0],
            'onTwigTemplatePaths' => ['onTwigTemplatePaths', 0],
            'onTwigSiteVariables' => ['onTwigSiteVariables', 0],
            'onFormProcessed' => ['onFormProcessed', 0]
        ];
    }

    /**
     * Initialize form if the page has one. Also catches form processing if user posts the form.
     */
    public function onPageInitialized()
    {
        /** @var Page $page */
        $page = $this->grav['page'];
        if (!$page) {
            return;
        }

        $header = $page->header();
        if (isset($header->form) && is_array($header->form)) {
            $this->active = true;

            // Create form.
            require_once __DIR__ . '/classes/form.php';
            $this->form = new Form($page);

            // Handle posting if needed.
            if (!empty($_POST)) {
                $this->form->post();
            }
        }
    }

        /**
     * Add current directory to twig lookup paths.
     */
    public function onTwigTemplatePaths()
    {
        $this->grav['twig']->twig_paths[] = __DIR__ . '/templates';
    }

    /**
     * Make form accessible from twig.
     */
    public function onTwigSiteVariables()
    {
        if (!$this->active) {
            return;
        }

        $this->grav['twig']->twig_vars['form'] = $this->form;
    }

    /**
     * Handle form processing instructions.
     *
     * @param Event $event
     */
    public function onFormProcessed(Event $event)
    {
        $form = $event['form'];
        $action = $event['action'];
        $params = $event['params'];

        if (!$this->active) {
            return;
        }

        if (!$this->validate($form)) {
            /** @var Language $l */
            $l = $this->grav['language'];
            $this->form->message = $l->translate('FORM_PLUGIN.NOT_VALIDATED');
            $uri = $this->grav['uri'];
            $route = $uri->route();

            /** @var Twig $twig */
            $twig = $this->grav['twig'];
            $twig->twig_vars['form'] = $form;

            /** @var Pages $pages */
            $pages = $this->grav['pages'];
            $page = $pages->dispatch($route, true);
            unset($this->grav['page']);
            $this->grav['page'] = $page;

            return;
        }

        $this->process($form);

        switch ($action) {
            case 'captcha':
                // Validate the captcha
                $query = http_build_query([
                    'secret' => $params['recatpcha_secret'],
                    'response' => $this->form->value('g-recaptcha-response')
                ]);
                $url = 'https://www.google.com/recaptcha/api/siteverify?'.$query;
                $response = json_decode(file_get_contents($url), true);

                if (!isset($response['success']) || $response['success'] !== true) {
                    throw new \RuntimeException('Error validating the Captcha');
                }
                break;
            case 'message':
                $this->form->message = (string) $params;
                break;
            case 'redirect':
                $this->grav->redirect((string) $params);
                break;
            case 'reset':
                if (in_array($params, array(true, 1, '1', 'yes', 'on', 'true'), true)) {
                    $this->form->reset();
                }
                break;
            case 'display':
                $route = (string) $params;
                if (!$route || $route[0] != '/') {
                    /** @var Uri $uri */
                    $uri = $this->grav['uri'];
                    $route = $uri->route() . ($route ? '/' . $route : '');
                }

                /** @var Twig $twig */
                $twig = $this->grav['twig'];
                $twig->twig_vars['form'] = $form;

                /** @var Pages $pages */
                $pages = $this->grav['pages'];
                $page = $pages->dispatch($route, true);
                unset($this->grav['page']);
                $this->grav['page'] = $page;
                break;
            case 'save':
                $prefix = !empty($params['fileprefix']) ? $params['fileprefix'] : '';
                $format = !empty($params['dateformat']) ? $params['dateformat'] : 'Ymd-His-u';
                $ext = !empty($params['extension']) ? '.' . trim($params['extension'], '.') : '.txt';
                $filename = !empty($params['filename']) ? $params['filename'] : '';
                $operation = !empty($params['operation']) ? $params['operation'] : 'create';

                if (!$filename) {
                    $filename = $prefix . $this->udate($format) . $ext;
                }

                /** @var Twig $twig */
                $twig = $this->grav['twig'];
                $vars = array(
                    'form' => $this->form
                );

                $fullFileName = DATA_DIR . $this->form->name . '/' . $filename;

                $file = File::instance($fullFileName);

                if ($operation == 'create') {
                    $body = $twig->processString(
                        !empty($params['body']) ? $params['body'] : '{% include "forms/data.txt.twig" %}',
                        $vars
                    );
                    $file->save($body);
                } elseif ($operation == 'add') {
                    $vars = $vars['form']->value();

                    foreach ($form->fields as $field) {
                        if (isset($field['process']) && isset($field['process']['ignore']) && $field['process']['ignore']) {
                            unset($vars[$field['name']]);
                        }
                    }

                    if (file_exists($fullFileName)) {
                        $data = Yaml::parse($file->content());
                        if (count($data) > 0) {
                            array_unshift($data, $vars);
                        } else {
                            $data[] = $vars;
                        }
                    } else {
                        $data[] = $vars;
                    }

                    $file->save(Yaml::dump($data));
                }
                break;
        }
    }

    /**
     * Validate a form
     *
     * @param Form $form
     * @return bool
     */
    protected function validate($form) {
        foreach ($form->fields as $field) {
            if (isset($field['validate']) && isset($field['validate']['required']) && $field['validate']['required']) {
                if (!$form->value($field['name'])) {
                    return false;
                }
            }
        }

        return true;
    }

    /**
     * Process a form
     *
     * Currently available processing tasks:
     *
     * - fillWithCurrentDateTime
     *
     * @param Form $form
     * @return bool
     */
    protected function process($form) {
        foreach ($form->fields as $field) {
            if (isset($field['process'])) {
                if (isset($field['process']['fillWithCurrentDateTime']) && $field['process']['fillWithCurrentDateTime']) {
                    $form->setValue($field['name'], gmdate('D, d M Y H:i:s', time()));
                }
            }
        }
    }

    /**
     * Create unix timestamp for storing the data into the filesystem.
     *
     * @param string $format
     * @param int $utimestamp
     * @return string
     */
    private function udate($format = 'u', $utimestamp = null)
    {
        if (is_null($utimestamp)) {
            $utimestamp = microtime(true);
        }

        $timestamp = floor($utimestamp);
        $milliseconds = round(($utimestamp - $timestamp) * 1000000);

        return date(preg_replace('`(?<!\\\\)u`', \sprintf('%06d', $milliseconds), $format), $timestamp);
    }
}
