def handle_pipeline_creation(request):
    # Extract build parameters from request
    build_parameters = request.get('buildParameters', [])
    
    # Validate and persist build parameters
    if validate_build_parameters(build_parameters):
        save_build_parameters_to_db(build_parameters)
    else:
        raise ValueError("Invalid build parameters")

