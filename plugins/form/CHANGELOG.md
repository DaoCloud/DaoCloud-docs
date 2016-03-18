# v1.1.0
## 12/18/2015

1. [](#new)
    * Croatian translation
    * Added id, style, and disabled options to select fields
1. [](#improved)
    * Allow adding form labels and help text as lang strings
    * Allow translating field content
    * Allow translating button and checkbox labels
    * Allow adding classes to the form field container with `field.outerclasses`
    * Updated French translation
1. [](#bugfix)
    * Fixed error message on file upload
    * Fixed overriding defaults for the file type in forms

# v1.0.3
## 12/11/2015

1. [](#improved)
    * Updated languages
    * Allow an action to stop processing
1. [](#bugfix)
    * Fix captcha validation
    * Fix issue where Form was unsetting valid page
        
# v1.0.2
## 12/01/2015

1. [](#bugfix)
    * Fixed merge of defaults settings
    * Support for arrays in `data.txt.twig`
    * Fixed blueprint for admin
    
# v1.0.1
## 12/01/2015

1. [](#new)
    * New **file upload** field
    * Added modular form template
    * Spanish translation
    * Hungarian translation
    * Italian translation

# v1.0.0
## 11/21/2015

1. [](#new)
    * Server-side validation of forms #11
    * Added french translation
    * Added **nonce** form security
1. [](#improved)
    * Show a more meaningful error when the display page is not found
    * Added links to learn site for form examples
    * Label can be omitted
    * Allow user to set the CSS class for buttons
1. [](#bugfix)
    * Fixed multi-language forms
    * Checkbox is translatable
    * Minor fixes

# v0.6.0
## 10/21/2015

1. [](#bugfix)
    * Fixed for missing attributes in textarea field
    * Fixed checkbox inputs

# v0.5.0
## 10/15/2015

1. [](#new)
	* New `operation` param to allow different file saving strategies
	* Ability to add new file saving strategies
	* Now calls a `process()` method during form processing
1. [](#improved)
    * Added server-side captcha validation and removed front-end validation
    * Allow `filename` instead of `prefix`, `format` + `extension`
1. [](#bugfix)
	* Fixed radio inputs

# v0.4.0
## 9/16/2015

1. [](#new)
	* PHP server-side form validation
    * Added new Google Catpcha field with front-end validation
1. [](#improved)
    * Add defaults for forms, moved from the themes to the Form plugin
    * Store multi-line fields with line endings converted to HTML

# v0.3.0
## 9/11/2015

1. [](#improved)
    * Refactored all the forms fields

# v0.2.1
## 08/24/2015

1. [](#improved)
    * Translated tooltips

# v0.2.0
## 08/11/2015

1. [](#improved)
    * Disable `enable` in admin

# v0.1.0
## 08/04/2015

1. [](#new)
    * ChangeLog started...
