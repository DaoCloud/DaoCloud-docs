<?php

namespace Grav\Plugin\Login;

interface ControllerInterface
{
    /**
     * Performs an action.
     */
    public function execute();

    /**
     * Redirects an action
     */
    public function redirect();
}
