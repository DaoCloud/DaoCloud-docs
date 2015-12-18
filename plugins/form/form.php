<?php
namespace Grav\Plugin;

use Grav\Common\Plugin;
use Symfony\Component\Yaml\Yaml;
use RocketTheme\Toolbox\File\File;
use RocketTheme\Toolbox\Event\Event;

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
            'onTwigSiteVariables' => ['onTwigSiteVariables', 0]
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
            require_once(__DIR__ . '/classes/form.php');
            $this->form = new Form($page);

            $this->enable([
                'onFormProcessed' => ['onFormProcessed', 0],
                'onFormValidationError' => ['onFormValidationError', 0]
            ]);

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
                    $this->grav->fireEvent('onFormValidationError', new Event(['form' => $form, 'message' => $this->grav['language']->translate('PLUGIN_FORM.ERROR_VALIDATING_CAPTCHA')]));
                    $event->stopPropagation();
                    return;
                }
                break;
            case 'message':
                $this->form->message = (string) $params;
                break;
            case 'redirect':
                $this->grav->redirect((string) $params);
                break;
            case 'reset':
                if (Utils::isPositive($params)) {
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

                if (!$page) {
                    throw new \RuntimeException('Display page not found. Please check the page exists.', 400);
                }

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

                $locator = $this->grav['locator'];
                $path = $locator->findResource('user://data', true);
                $fullFileName = $path . DS . $this->form->name . DS . $filename;

                $file = File::instance($fullFileName);

                if ($operation == 'create') {
                    $body = $twig->processString(
                        !empty($params['body']) ? $params['body'] : '{% include "forms/data.txt.twig" %}',
                        $vars
                    );
                    $file->save($body);
                } elseif ($operation == 'add') {
                    $vars = $vars['form']->value()->toArray();

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
     * Handle form validation error
     *
     * @param  Event  $event An event object
     */
    public function onFormValidationError(Event $event)
    {
        $form = $event['form'];
        if (empty($form->message)) {
            $form->message = $event['message'];
        }

        $uri = $this->grav['uri'];
        $route = $uri->route();

        /** @var Twig $twig */
        $twig = $this->grav['twig'];
        $twig->twig_vars['form'] = $form;

        /** @var Pages $pages */
        $pages = $this->grav['pages'];
        $page = $pages->dispatch($route, true);

        if ($page) {
            unset($this->grav['page']);
            $this->grav['page'] = $page;
        }

        $event->stopPropagation();
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
