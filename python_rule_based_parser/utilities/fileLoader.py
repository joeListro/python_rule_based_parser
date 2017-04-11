from python_rule_based_parser.model.pythonCodeModel import pythonCodeModel

class fileLoader:
    """Load text from file"""

    def __init__(self):
        return super().__init__()

    def load_file(self, pathToFile):
        
        code = []
        
        with open (pathToFile, "r") as file:
            code = file.readlines()

        python_code = pythonCodeModel(code)

        return python_code