class file_IO:
    """Load text from file"""

    def __init__(self):

        return super().__init__()

    def input(self, path_to_file):
        
        code = []
        
        with open (path_to_file, "r") as file:
            code = file.readlines()

        return code

    def output(self, path_to_file, parsed_code):

        with open (path_to_file, "w") as file:

            file.write("\n".join(parsed_lines))