class tokenizer:
    """"Tokenizes a code string"""

    def __init__(self, codeToTokenize):

        self.code = codeToTokenize

        return super().__init__()

    def tokenize(self):

        tokens = []

        currentToken = ''

        for letter in self.code:
            if self.isSegueChar(letter):
                newToken = 'Token 01:' + currentToken
                tokens.append(newToken)
                currentToken = ""

            if self.isSingleToken(letter):
                newToken = 'Token 02:' + letter
                tokens.append(newToken)

            else:
                currentToken += letter

        return '\r'.join(tokens)

    def isSegueChar(self, currentChar):

        if (self.isSpaceOrTab(currentChar) or self.isNewLine(currentChar) or self.isCarriageReturn(currentChar)):
            return True
        else:
            return False

    def isSpaceOrTab(self, currentChar):

        if (currentChar == ' '):
            return True
        elif (currentChar == '\t'):
            return True
        else:
            return False

    def isNewLine(self, currentChar):

        if (currentChar == '\n'):
            return True
        else:
            return False

    def isCarriageReturn(self, currentChar):

        if (currentChar == '\r'):
            return True
        else:
            return False

    def isSingleToken(self, currentChar):

        if (currentChar == '{'):
            return True
        elif (currentChar == '}'):
            return True
        elif (currentChar == '['):
            return True
        elif (currentChar == ']'):
            return True
        elif (currentChar == '('):
            return True
        elif (currentChar == ')'):
            return True
        elif (self.isComparisonOperator(currentChar)):
            return True
        else:
            return False

    def isComparisonOperator(self, currentChar):

        if(currentChar == '=='):
            return True
        elif(currentChar == '<='):
            return True
        elif(currentChar == '>='):
            return True
        elif(currentChar == '<'):
            return True
        elif(currentChar == '>'):
            return True
        elif(currentChar == '||'):
            return True
        elif(currentChar == '&&'):
            return True
        else:
            return False