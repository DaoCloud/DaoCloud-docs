<?php
namespace Grav\Plugin;

use Grav\Common\Filesystem\Folder;
use Grav\Common\Iterator;
use Grav\Common\GravTrait;
use Grav\Common\Page\Page;
use Grav\Common\Data\Data;
use Grav\Common\Data\Blueprint;
use Grav\Common\Utils;
use RocketTheme\Toolbox\Event\Event;

class Form extends Iterator
{
    use GravTrait;

    /**
     * @var string
     */
    public $message;

    /**
     * @var array
     */
    protected $data = array();

    /**
     * @var array
     */
    protected $rules = array();

    /**
     * @var array
     */
    protected $items = array();

    /**
     * @var array
     */
    protected $values = array();

    /**
     * @var Page $page
     */
    protected $page;

    /**
     * Create form for the given page.
     *
     * @param Page $page
     */
    public function __construct(Page $page)
    {
        $this->page = $page;

        $header      = $page->header();
        $this->rules = isset($header->rules) ? $header->rules : array();
        $this->data  = isset($header->data) ? $header->data : array();
        $this->items = $header->form;

        // Set form name if not set.
        if (empty($this->items['name'])) {
            $this->items['name'] = $page->slug();
        }

        $this->reset();

        // Fire event
        self::getGrav()->fireEvent('onFormInitialized', new Event(['form' => $this]));
    }

    /**
     * Reset values.
     */
    public function reset()
    {
        $name = $this->items['name'];

        // Fix naming for fields (presently only for toplevel fields)
        foreach ($this->items['fields'] as $key => $field) {
            if (is_numeric($key) && isset($field['name'])) {
                unset($this->items['fields'][$key]);

                $key                         = $field['name'];
                $this->items['fields'][$key] = $field;
            }
        }

        $blueprint    = new Blueprint($name, ['form' => $this->items, 'rules' => $this->rules]);
        $this->values = new Data($this->data, $blueprint);
    }

    /**
     * Return page object for the form.
     *
     * @return Page
     */
    public function page()
    {
        return $this->page;
    }

    /**
     * Get value of given variable (or all values).
     *
     * @param string $name
     *
     * @return mixed
     */
    public function value($name = null)
    {
        if (!$name) {
            return $this->values;
        }
        return $this->values->get($name);
    }

    /**
     * Set value of given variable.
     *
     * @param string $name
     *
     * @return mixed
     */
    public function setValue($name = null, $value = '')
    {
        if (!$name) {
            return;
        }

        $this->values->set($name, $value);
    }

    /**
     * Handle form processing on POST action.
     */
    public function post()
    {
        $files = [];
        if (isset($_POST)) {
            $values = (array)$_POST;
            $files  = (array)$_FILES;

            if (method_exists('Grav\Common\Utils', 'getNonce')) {
                if (!isset($values['form-nonce']) || !Utils::verifyNonce($values['form-nonce'], 'form')) {
                    $event = new Event(['form' => $this, 'message' => self::getGrav()['language']->translate('PLUGIN_FORM.NONCE_NOT_VALIDATED')]);
                    self::getGrav()->fireEvent('onFormValidationError', $event);
                    return;
                }
            }

            unset($values['form-nonce']);

            foreach ($this->items['fields'] as $field) {
                $name = $field['name'];
                if ($field['type'] == 'checkbox') {
                    $values[$name] = isset($values[$name]) ? true : false;
                }
            }


            // Add post values to form dataset
            $this->values->merge($values);
            $this->values->merge($files);
        }

        // Validate and filter data
        try {
            $this->values->validate();
            $this->values->filter();

            foreach ($files as $key => $file) {
                $cleanFiles = $this->cleanFilesData($key, $file);
                if ($cleanFiles) {
                    $this->values->set($key, $cleanFiles);
                }
            }

            self::getGrav()->fireEvent('onFormValidationProcessed', new Event(['form' => $this]));
        } catch (\RuntimeException $e) {
            $event = new Event(['form' => $this, 'message' => $e->getMessage()]);
            self::getGrav()->fireEvent('onFormValidationError', $event);
            if ($event->isPropagationStopped()) {
                return;
            }
        }

        $process = isset($this->items['process']) ? $this->items['process'] : array();
        if (is_array($process)) {
            $event = null;
            foreach ($process as $action => $data) {
                if (is_numeric($action)) {
                    $action = \key($data);
                    $data   = $data[$action];
                }

                $previousEvent = $event;
                $event = new Event(['form' => $this, 'action' => $action, 'params' => $data]);

                if ($previousEvent) {
                    if (!$previousEvent->isPropagationStopped()) {
                        self::getGrav()->fireEvent('onFormProcessed', $event);
                    }
                } else {
                    self::getGrav()->fireEvent('onFormProcessed', $event);
                }
            }
        } else {
            // Default action.
        }
    }

    private function cleanFilesData($key, $file)
    {
        $config  = self::getGrav()['config'];
        $default = $config->get('plugins.form.files');
        $settings = isset($this->items['fields'][$key]['files']) ? $this->items['fields'][$key]['files'] : [];

        /** @var Page $page */
        $page             = null;
        $blueprint        = array_merge_recursive($default, $settings);
        $cleanFiles[$key] = [];
        if (!isset($blueprint)) {
            return false;
        }

        $cleanFiles = [$key => []];
        foreach ((array)$file['error'] as $index => $error) {
            if ($error == UPLOAD_ERR_OK) {
                $tmp_name    = $file['tmp_name'][$index];
                $name        = $file['name'][$index];
                $type        = $file['type'][$index];
                $destination = Folder::getRelativePath(rtrim($blueprint['destination'], '/'));

                if (!$this->match_in_array($type, $blueprint['accept'])) {
                    throw new \RuntimeException('File "' . $name . '" is not an accepted MIME type.');
                }

                if (Utils::startsWith($destination, '@page:')) {
                    $parts = explode(':', $destination);
                    $route = $parts[1];
                    $page  = self::getGrav()['page']->find($route);

                    if (!$page) {
                        throw new \RuntimeException('Unable to upload file to destination. Page route not found.');
                    }

                    $destination = $page->relativePagePath();
                } else if ($destination == '@self') {
                    $page        = self::getGrav()['page'];
                    $destination = $page->relativePagePath();
                } else {
                    Folder::mkdir($destination);
                }

                if (move_uploaded_file($tmp_name, "$destination/$name")) {
                    $path                    = $page ? self::getGrav()['uri']->convertUrl($page, $page->route() . '/' . $name) : $destination . '/' . $name;
                    $cleanFiles[$key][$path] = [
                        'name'  => $file['name'][$index],
                        'type'  => $file['type'][$index],
                        'size'  => $file['size'][$index],
                        'file'  => $destination . '/' . $name,
                        'route' => $page ? $path : null
                    ];
                } else {
                    throw new \RuntimeException("Unable to upload file(s) to $destination/$name");
                }
            }
        }

        return $cleanFiles[$key];
    }

    private function match_in_array($needle, $haystack)
    {
        foreach ((array)$haystack as $item) {
            if (true == preg_match("#^" . strtr(preg_quote($item, '#'), array('\*' => '.*', '\?' => '.')) . "$#i", $needle)) {
                return true;
            }
        }

        return false;
    }
}
