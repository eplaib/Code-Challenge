import string

class Res:
    '''
    This class classifies each element of the RNAm sequence:
        type (string): It can be a codon, InvalidChar, InvalidLength, UnexpectedEnd or gen
        cod (string): It's none by default. If we found a codon, then we record it here 
        error (boolean): It's false by default. If we found an error, then we write True
        error_atr (list): It's None by default. If we found an invalid character,
                          then we write the line and the position 
        gen (list): It's None by default. If we found a complete gen, then we record it here
    '''

    def __init__(self, type, cod = None, error = False, error_atr = None, gen = None):
        self.type = type
        self.cod = cod
        self.error = error
        if error_atr is None:
            self.error_atr = []
        else:
            self.error_atr = error_atr
        if gen is None:
            self.gen = []
        else:
            self.gen = gen


    def _InvalidChar(self):
        return 'Invalid characteres. There is an invalid character in line {0},\
        position {1}'.format(self.error_atr[0], self.error_atr[1])

    def _InvalidLength(self):
        return 'Invalid string length. Each codon should have 3 nucleotides'
    
    def _UnexpectedEnd(self):
        return 'Unexpected end of gene. There is not stop codon at the end of the string'

    
    

