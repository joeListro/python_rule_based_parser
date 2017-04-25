class tokenizer:
    """"Tokenizes a code string"""

    def __init__(self, codeToTokenize):

        self.code = codeToTokenize

        return super().__init__()

    def tokenize(self):

        tokens = []

        currentToken = ''

        notSingleLineComment = True

        notMultiLineComment = True

        self.lineNumbers = 1

        for letter in self.code:

            currentToken += letter

            if (notSingleLineComment):

                if (notMultiLineComment):

                    if (self.isSingleLineComment(currentToken)):


                        notSingleLineComment = False

                        currentToken = ''

                    elif (self.isMultiLineCommentBegin(currentToken)):

                        notMultiLineComment = False

                        currentToken = ''

                    elif (self.isSegueToken(currentToken)):

                        currentToken = ''

                    elif (self.isSingleToken(currentToken)):

                        newToken = 'Token 02:' + currentToken

                        print(newToken)

                        tokens.append(newToken)

                        currentToken = ''

                    elif (self.isSingleToken(letter)):

                        if (not self.isSegueToken(currentToken)):

                            currentToken = currentToken[:-1]

                            newToken = 'Token 01:' + currentToken

                            print(newToken)

                            tokens.append(newToken)

                        newToken = 'Token 02:' + letter

                        print(newToken)

                        tokens.append(newToken)

                        currentToken = ''

                    elif (self.isSegueToken(letter)):

                        if (self.isDoubleToken(currentToken)):

                            currentToken = currentToken[:-1]

                            newToken = 'Token 04:' + currentToken

                            print(newToken)

                            tokens.append(newToken)

                            currentToken = ''

                        elif (not self.isSegueToken(currentToken)):

                            currentToken = currentToken[:-1]

                            newToken = 'Token 01:' + currentToken

                            print(newToken)

                            tokens.append(newToken)

                            currentToken = ''

                elif (self.isMultiLineCommentEnd(currentToken)):

                    notMultiLineComment = True

                    currentToken = ''

                elif (letter == '*'):

                    currentToken = letter

            elif (self.isNewLine(currentToken)):

                notSingleLineComment = True

                currentToken = ''

        lineNumbersToken = 'Total Number of Lines:' + str(self.lineNumbers)

        tokens.append(lineNumbersToken)

        tokens.append('**** End of Tokenizer ****')

        for token in tokens:

            print(token)

        return '\n'.join(tokens)

    def isSegueToken(self, currentToken):

        if (self.isSpace(currentToken) or self.isTab(currentToken) or self.isNewLine(currentToken)):
  
            return True
  
        else:
  
            return False

    def isSpace(self, currentToken):

        if (currentToken == ' '):
  
            return True
  
        else:
  
            return False

    def isTab(self, currentToken):
        
        if (currentToken == '\t'):
  
            return True
  
        else:
  
            return False

    def isNewLine(self, currentToken):
        
        if ((currentToken == '\n') or (currentToken == '\r')):

            self.lineNumbers += 1

            return True

        else:
            return False

    def isSingleToken(self, currentToken):

        if (currentToken == '{'):

            return True

        elif (currentToken == '}'):

            return True

        elif (currentToken == '['):

            return True

        elif (currentToken == ']'):

            return True

        elif (currentToken == '('):

            return True

        elif (currentToken == ')'):

            return True

        elif (currentToken == '<'):

            return True

        elif (currentToken == '>'):

            return True

        elif (currentToken == '.'):

              return True

        elif (currentToken == ';'):

            return True

        else:

            return False


    def isDoubleToken(self, currentToken):

        if (currentToken == '=='):

            return True

        elif (currentToken == '<='):

            return True

        elif (currentToken == '>='):

            return True

        elif (currentToken == '||'):

            return True

        elif (currentToken == '&&'):

            return True

        else:

            return False


    def isSingleLineComment(self, currentToken):

        if (currentToken == '//'):
 
            return True
 
        else:
 
            return False

    def isMultiLineCommentBegin(self, currentToken):
        
        if (currentToken == '/*'):

            return True

        else:

            return False

    def isMultiLineCommentEnd(self, currentToken):

        if (currentToken == '*/'):

            return True

        else:

            return False