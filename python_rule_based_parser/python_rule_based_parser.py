from pypeg2 import parse

from python_rule_based_parser.utilities.fileLoader import fileLoader

class python_rule_based_parser:

    def __init__(self):
        
        return super().__init__()

    def __parse__(self, file):
        
        file_loader = fileLoader(file)
        
        python_code = file_loader.load_file(file) # fileLoader.load_file() returns a pythonCodeModel object

        # Scan the python_code

        tokenize = tokenizer()

        tokenize.tokenize()

        # Parse the information returned by the tokenizer

        return