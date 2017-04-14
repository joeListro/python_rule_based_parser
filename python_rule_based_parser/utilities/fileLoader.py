class fileLoader:
    """Load text from file"""

    def __init__(self):
        return super().__init__()

    def load_file(self, pathToFile):
        
        code = []
        
        with open (pathToFile, "r") as file:
            code = file.readlines()

        return code