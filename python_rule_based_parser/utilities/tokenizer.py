class tokenizer:
    """"Tokenizes a code string"""

    def __init__(self, codeToTokenize):

        self.code = codeToTokenize

        return super().__init__()

    def tokenize(self):

        tokens = []

        currentToken = "Token 0:"

        tokenNumber = 0

        for letter in self.code:
            if self.isSegueChar(letter):
                tokens.append(currentToken)
                tokenNumber = tokenNumber + 1
                currentToken = "Token " + str(tokenNumber) + ":"

            if self.isSingleToken(letter):
                tokens.append(currentToken)
                tokenNumber = tokenNumber + 1
                currentToken = "Token " + str(tokenNumber) + ":"
                tokens.append("Token " + str(tokenNumber) + ":" + letter)
                tokenNumber = tokenNumber + 1
            else:
                currentToken += letter

        return tokens

    def isSegueChar(self, currentChar):

        if (self.isSpaceOrTab(currentChar) or self.isNewLine(currentChar) or self.isCarriageReturn(currentChar)):
            return True

        return False

    def isSpaceOrTab(self, currentChar):

        if (currentChar == ' '):
            return True
        if (currentChar == '\t'):
            return True

        return False

    def isNewLine(self, currentChar):

        if (currentChar == '\n'):
            return True
        
        return False

    def isCarriageReturn(self, currentChar):

        if (currentChar == '\r'):
            return True

        return False

    def isSingleToken(self, currentChar):

        if (currentChar == '{'):
            return True
        if (currentChar == '}'):
            return True
        if (currentChar == '['):
            return True
        if (currentChar == ']'):
            return True
        if (currentChar == '('):
            return True
        if (currentChar == ')'):
            return True
        if (self.isComparisonOperator(currentChar)):
            return True

        return False

    def isComparisonOperator(self, currentChar):

        if(currentChar == "=="):
            return True
        if(currentChar == "<="):
            return True
        if(currentChar == ">="):
            return True
        if(currentChar == "<"):
            return True
        if(currentChar == ">"):
            return True
        if(currentChar == "||"):
            return True
        if(currentChar == "&&"):
            return True