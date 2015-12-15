<?php
namespace Grav\Plugin;

use Grav\Common\Iterator;
use Grav\Common\Grav;
use Grav\Common\Page\Page;

class GitHub extends Iterator {

    protected $page;
    public $client;
    public $paginator;

    public function __construct() {
        require_once __DIR__ . '/../vendor/autoload.php';

        $this->client = new \Github\Client(
                            new \Github\HttpClient\CachedHttpClient(array('cache_dir' => CACHE_DIR . '/github'))
                        );
        $this->paginator = new \Github\ResultPager($this->client);
    }
}
