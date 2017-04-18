class tokenizer:
    """"Tokenizes a code string"""

    def __init__(self, codeToTokenize):

        self.code = codeToTokenize

        return super().__init__()

    def tokenize(self):

        tokens = []

        currentToken = "Token00:"

        for letter in self.code:
            if self.isSegueChar(letter):
                tokens.append(currentToken)
                currentToken = "Token00:"

            if self.isSingleToken(letter):
                tokens.append(currentToken)
                currentToken = "Token00:"
                tokens.append("Token00:" + letter)

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