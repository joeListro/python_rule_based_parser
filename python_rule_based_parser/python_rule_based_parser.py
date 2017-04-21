from pypeg2 import parse

from utilities.file_IO import file_IO
from utilities.tokenizer import tokenizer
import python_rule_based_parser



class python_rule_based_parser:

    def __init__(self):

        self.code_string = ""

        self.parsed_code = []
        
        return super().__init__()

    def parse(self, file):
        
        fileIO = file_IO()
        
        self.code_string = fileIO.input(file) 

        tokenizer = tokenizer(self.code_string)

        self.parsed_code = tokenizer.tokenize()

        fileIO.output(file, self.parsed_code)

        return


if __name__ == '__main__':
    print('Welcome to Alex, Ben, and Joe\'s Parser\n')
    print('---------------------------------------\n')
    file = input('Enter a path to the file you want to parse : ')
    parser = python_rule_based_parser()
    parser.parse(file)