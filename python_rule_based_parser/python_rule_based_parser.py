from pypeg2 import parse

from utilities.file_IO import file_IO
from utilities.tokenizer import tokenizer

def parse(file):
       
    fileIO = file_IO()
        
    code_string = fileIO.input(file)

    parsed_code = tokenizer(code_string).tokenize()

    fileIO.output('output.txt', parsed_code)

    return

if __name__ == '__main__':
    print('Welcome to Alex, Ben, and Joe\'s Parser\n')
    print('---------------------------------------\n')
    file = input('Enter a path to the file you want to parse : ')

    parse(file)