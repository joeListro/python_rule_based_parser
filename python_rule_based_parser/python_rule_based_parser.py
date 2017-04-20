from pypeg2 import parse

from utilities.file_IO import file_IO
from utilities.tokenizer import tokenizer

class python_rule_based_parser:

    def __init__(self):

        self.code_string = ""

        self.parsed_code = []
        
        return super().__init__()

    def __parse__(self, file):
        
        fileIO = file_IO(file)
        
        self.code_string = fileIO.input(file) 

        tokenizer = tokenizer(self.code_string)

        self.parsed_code = tokenizer.tokenize()

        fileIO.output(file, self.parsed_code)

        return