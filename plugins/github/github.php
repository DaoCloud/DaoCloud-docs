<?php
namespace Grav\Plugin;

use Grav\Common\Plugin;
use Grav\Common\Page\Page;
use Grav\Common\Grav;

class GitHubPlugin extends Plugin
{
    protected $active = false;
    protected $github;

    /**
     * @return array
     */
    public static function getSubscribedEvents()
    {
        return [
            'onPluginsInitialized' => ['onPluginsInitialized', 0]
        ];
    }

    /**
     * Initialize configuration
     */
    public function onPluginsInitialized()
    {
        if ($this->isAdmin()) {
            $this->active = false;
            return;
        }

        $this->enable([
            'onTwigTemplatePaths' => ['onTwigTemplatePaths', 0],
            'onPageInitialized' => ['onPageInitialized', 0]
        ]);
    }

    /**
     * Add current directory to twig lookup paths.
     */
    public function onTwigTemplatePaths()
    {
        $this->grav['twig']->twig_paths[] = __DIR__ . '/templates';
    }

    /**
     * Initialize github when detected in a page.
     */
    public function onPageInitialized()
    {
        $page = $this->grav['page'];
        if (!$page) {
            return;
        }

        if (isset($page->header()->github)) {
            $this->active = true;
            $config = $this->grav['config'];

            $method = $config->get('plugins.github.auth.method');
            $token = $config->get('plugins.github.auth.token');
            $passwd = $config->get('plugins.github.auth.password');

            // Initialize GitHub API Class
            require_once __DIR__ . '/classes/github.php';
            $this->github = new GitHub($page);

            if ($method && $token) {
                switch($method) {
                    case 'api':
                        $method = \Github\Client::AUTH_URL_TOKEN;
                        $passwd = null;
                        break;
                    case 'password':
                        $method = \Github\Client::AUTH_HTTP_PASSWORD;
                        break;
                }

                $this->github->client->authenticate($token, $passwd, $method);
            }

            $this->enable([
                'onTwigSiteVariables' => ['onTwigSiteVariables', 0]
            ]);

        }
    }




    /**
     * Make form accessible from twig.
     */
    public function onTwigSiteVariables()
    {
        // in Twig template: {{ github.client.api('repo').show('getgrav', 'grav')['stargazers_count'] }}
        $this->grav['twig']->twig_vars['github'] = $this->github;
    }
}
