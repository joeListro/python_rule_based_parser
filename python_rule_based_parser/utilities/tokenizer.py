class tokenizer:
    """"Tokenizes a code string"""

    def __init__(self, codeToTokenize):

        self.code = codeToTokenize

        return super().__init__()

    def tokenize(self):

        tokens = []

        currentToken = ''

        for letter in self.code:
            print('letter : ' + letter)

            if (self.isSegueChar(letter)):
                if (self.isComparisonOperator(currentToken)):
                    newToken = 'Token 04:' + currentToken
                    tokens.append(newToken)
                    currentToken = ''
                elif (self.isSingleToken(currentToken)):
                    newToken = 'Token 02:' + currentToken
                    tokens.append(newToken)
                    currentToken = ''
                else:
                    newToken = 'Token 01:' + currentToken
                    tokens.append(newToken)
                    currentToken = ''
            elif (not self.isSegueChar(letter)):
                currentToken += letter

        return '\n'.join(tokens)

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