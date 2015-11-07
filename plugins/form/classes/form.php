<?php
namespace Grav\Plugin;

use Grav\Common\Iterator;
use Grav\Common\Grav;
use Grav\Common\GravTrait;
use Grav\Common\Page\Page;
use RocketTheme\Toolbox\Event\Event;

class Form extends Iterator
{
    use GravTrait;

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

        $header = $page->header();
        $this->rules = isset($header->rules) ? $header->rules : array();
        $this->data = isset($header->data) ? $header->data : array();
        $this->items = $header->form;

        // Set form name if not set.
        if (empty($this->items['name'])) {
            $this->items['name'] = $page->slug();
        }
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
     * @return mixed
     */
    public function value($name = null)
    {
        if (!$name) {
            return $this->values;
        }
        return $this->getField($name, 'values');
    }

    /**
     * Get value of given variable (or all values).
     *
     * @param string $name
     * @return mixed
     */
    public function setValue($name = null, $value = '')
    {
        if (!$name) {
            return;
        }

        $this->values[$name] = $value;
    }

    /**
     * Reset values.
     */
    public function reset()
    {
        $this->values = array();
    }

    /**
     * Handle form processing on POST action.
     */
    public function post()
    {
        if (isset($_POST)) {
            $this->values = (array) $_POST;
        }

        foreach($this->items['fields'] as $field) {
            if ($field['type'] == 'checkbox') {
                if (isset($this->values[$field['name']])) {
                    $this->values[$field['name']] = true;
                } else {
                    $this->values[$field['name']] = false;
                }
            }
        }

        $process = isset($this->items['process']) ? $this->items['process'] : array();
        if (is_array($process)) {
            foreach ($process as $action => $data) {
                if (is_numeric($action)) {
                    $action = \key($data);
                    $data = $data[$action];
                }
                self::getGrav()->fireEvent('onFormProcessed', new Event(['form' => $this, 'action' => $action, 'params' => $data]));
            }
        } else {
            // Default action.
        }
    }


    /**
     * @param string $name
     * @param string $scope
     * @return mixed|null
     * @internal
     */
    protected function getField($name, $scope = 'value')
    {
        $path = explode('.', $name);

        $current = $this->{$scope};
        foreach ($path as $field) {
            if (is_object($current) && isset($current->{$field})) {
                $current = $current->{$field};
            } elseif (is_array($current) && isset($current[$field])) {
                $current = $current[$field];
            } else {
                return null;
            }
        }

        return $current;
    }
}
