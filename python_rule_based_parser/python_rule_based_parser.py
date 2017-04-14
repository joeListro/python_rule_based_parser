from pypeg2 import parse

from python_rule_based_parser.utilities.fileLoader import fileLoader

class python_rule_based_parser:

    def __init__(self):

        self.python_code = ""
        
        return super().__init__()

    def __parse__(self, file):
        
        file_loader = fileLoader(file)
        
        self.python_code = file_loader.load_file(file) 

        # Scan the python_code

        tokenize = tokenizer(self.python_code)

        tokenize.tokenize()

        # Parse the information returned by the tokenizer

        return