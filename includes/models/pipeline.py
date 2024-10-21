class Pipeline:
    def __init__(self, name, build_parameters=None):
        self.name = name
        self.build_parameters = build_parameters or []

    def save(self):
        # Logic to save the pipeline and its build parameters to the database
        pass

    
