from pypeg2 import parse

from utilities.file_IO import file_IO
from utilities.tokenizer import tokenizer

def parse(file):
        
    fileIO = file_IO()
        
    code_string = fileIO.input(file)

    print(code_string)
    parsed_code = tokenizer(code_string).tokenize()

	print(parsed_code)

    fileIO.output('output.txt', parsed_code)

    return
if __name__ == '__main__':
    print('Welcome to Alex, Ben, and Joe\'s Parser\n')
    print('---------------------------------------\n')
    file = input('Enter a path to the file you want to parse : ')
    parser = python_rule_based_parser()
    parser.parse(file)