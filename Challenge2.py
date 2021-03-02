import re, click
import io
from Classes.Codon import CodonType


@click.command()
@click.argument('file', nargs = 1)
def main(file):

    string = open(file, 'r', buffering=1)

    for gene in Gene_Creation(string):
        print(gene)



def Gene_Creation(string):
    '''
    This function creates the different genes. Check if each codon is correct. In case a final 
    codon is found, then this gene is completed. 
    '''
    codon = CodonType()
    codon.Codon_Clasification()

    Gene = []

    for cod in Read_String(string):
        
        if (cod in codon.normal_codon):
            Gene.append(cod)

        elif(cod in codon.stop_codon):
            #If there are one or more elements in the Gene list, then we found a complete gen; Otherwise there is a sequence of stop codons
            if len(Gene) > 0:
                Gene.append(cod)
                yield Gene
                Gene = []
            else:
                continue
                
        elif cod[0] == 'Error':
            yield 'Invalid characteres. There is an invalid character in line {0} position {1}'.format(cod[1], cod[2])
            Gene = []
            break

        elif len(cod) < 3:
            yield 'Invalid string length. The last gen has not a valid string length. Each codon should have 3 nucleotides'
            Gene = []
            break
    
    #If the last gen has not an stop codon, then there is an error 
    if len(Gene) > 0:
        yield 'Unexpected end of gene. The last gen has not stop codon at the end of the string'
        


def Read_String(string):
    '''
    This function reads reads line by line the string and separates its codons.
    Whitespace characters are ignored. If there is a >, then goes to next line.
    The last group of elements is sended even there is no 3 elements.
    '''

    cod = ''

    for l, line in enumerate(string):
        for pos, el in enumerate(line):
            #Check if there is a whitespace. If yes ignore it and go to next character
            if re.match(r'\s', el):
                continue
            #Check if there is a >. If yes ignore it and go to next line
            elif el == '>':
                break
            #Check if the is a A,U,C,G character. If yes add it to the cod string until its length is 3
            elif re.match('[AUCG]', el.upper()):
                cod = cod + el.upper()
                if(len(cod) == 3):
                    yield cod
                    cod = ''
            else:
                Error = ['Error', l, pos]
                yield Error 
            
    #If the last codon has 1 or 2 character, then the string has an invalid length
    if(cod != ''):
        yield cod          

if __name__ == '__main__':
    main()