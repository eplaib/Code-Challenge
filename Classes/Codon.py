import string
import itertools

class CodonType:
    '''
    Codon_Type contains and classify all the possible codons in two types:
    normal_codon and stop_codon
    '''

    def __init__(self):
        self.codon = []
        self.normal_codon = []
        self.stop_codon = []

    #Creating all possible codon combinations
    def Codon_List(self):
        list_codon = [p for p in itertools.product('AUCG', repeat=3)]
        for i in list_codon:
            self.codon.append(i[0] + i[1] + i[2])
    
    #Clasifying each codon as normal_codon or stop_codon
    def Codon_Clasification(self):

        self.Codon_List()

        for i in self.codon:
            if i == 'UAG' or i == 'UGA' or i == 'UAA':
                self.stop_codon.append(i)
            else:
                self.normal_codon.append(i)
        
        return self.normal_codon, self.stop_codon