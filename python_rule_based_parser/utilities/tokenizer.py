class tokenizer:
    """"Tokenizes a code string"""

    def __init__(self, codeToTokenize):

        self.code = codeToTokenize

        return super().__init__()

    def tokenizer(self):

        # Loop through self.code to find interesting events.

        return

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

        return False

    def isDoubleToken(self, currentChar):

        if (currentChar == '{'):
            return False

        return True

    def isIdentifierChar(self, currentChar):

        if(self.isSingleToken(currentChar) or self.isSpaceOrTab(currentChar) or self.isNewLine(currentChar) or self.isCarriageReturn(currentChar)):
            return False

        return True