# v1.2.1
## 12/18/2015

1. [](#new)
    * Croatian translation
1. [](#improved)
    * Use type `email` in registration form
    * Drop manual validation in registration

# v1.2.0
## 12/11/2015

1. [](#new)
    * Added account activation email upon registration
    * Added forgot password functionality
    * Support ACL from parent page
    * Allow login immediately after account activation
1. [](#improved)
    * Handle admin login page if available
    * Example registration form now provided by plugin
    * Better error handling of registration
    * Tab-based plugin configuration
    * Updated translations
1. [](#bugfix)
    * Prevent failing when no default values are set

# v1.1.0
## 12/01/2015

1. [](#new)
    * Support new **User Registration**
1. [](#improved)
    * Use new security salt for newer and fallback otherwise
    * Composer update of libraries
    * Check for session existence else throw a runtime error
1. [](#bugfix)
    * Fix remember-me functionality
    * Check page exists so as not to fail hard
    * Fix for static Inflector references #17

    
# v1.0.1
## 11/23/2015

1. [](#improved)
    * Hardening cookies with user-agent and system cache key instead of deprecated system hash
    * Set a custom route for login only if it's not an admin path

# v1.0.0
## 11/21/2015

1. [](#new)
    * Added OAuth login support for _Facebook_, _Google_, _GitHub_ and _Twitter_
    * Added **Nonce** form security support
    * Added option to "redirect after login"
    * Added "remember me" functionality
    * Added Hungarian translation
2. [](#improved)
    * Added blueprints for Grav Admin plugin (multi-language support!)

# v0.3.3
## 09/11/2015

1. [](#improved)
    * Changed authorise to authorize
1. [](#bugfix)
    * Fix denied string

# v0.3.2
## 09/01/2015

1. [](#improved)
    * Broke out login form into its own partial

# v0.3.1
## 08/31/2015

1. [](#improved)
    * Added username field autofocus

# v0.3.0
## 08/24/2015

1. [](#new)
    * Added simple CSS styling
    * Added simple login status with logout
1. [](#improved)
    * Improved README documentation
    * More strings translated
    * Updated blueprints

# v0.2.0
## 08/11/2015

1. [](#improved)
    * Disable `enable` in admin

# v0.1.0
## 08/04/2015

1. [](#new)
    * ChangeLog started...
