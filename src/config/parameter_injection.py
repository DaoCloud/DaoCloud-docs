def inject_parameters(config, parameters):
    """
    Injects parameters into the configuration template.

    :param config: The configuration template as a dictionary.
    :param parameters: A dictionary of parameters to inject.
    :return: The updated configuration with parameters injected.
    """
    for key, value in parameters.items():
        if key in config:
            config[key] = value
    return config

# Example usage
config_template = {'endpoint': '/api/rest-eventbus', 'method': 'POST'}
parameters = {'method': 'GET'}
updated_config = inject_parameters(config_template, parameters)
