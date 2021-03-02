import click
import re
from Classes.Codon import CodonType
from Classes.results import Res

@click.command()
@click.argument('name', nargs = 1)
def main(name):

    if checkFileExistance(name):
        file = open(name, encoding='utf-8')
        string = file.read()
    else:
        string = name

    Genes = Genes_List(string)
    print(Genes)


def checkFileExistance(file):
    '''
    This functions checks if the file exists or not
    '''
    try:
        with open(file, 'r'):
            return True
    except FileNotFoundError:
        return False
    except IOError:
        return False


def Genes_List(string):
    '''
    This function creates a list of genes. If a gen is correct, then its added to the list. 
    In case there is a error we print the error
    '''

    Genes = []

    for gen in Gen_Creation(string):
        #If the input is classify as 'Gen', add it to the Genes list, otherwise is an error
        if gen.type == 'Gen':
            Genes.append(gen.gen[:])
        else:
            if gen.type == 'InvalidLength':
                return gen._InvalidLength()
            elif gen.type == 'UnexpectedEnd':
                return gen._UnexpectedEnd()
            else:
                return gen._InvalidChar()
            break
    
    return Genes


def Gen_Creation(string):
    '''
    This function creates the different genes. Check if each codon is correct. In case a final 
    codon is found, then this gene is completed. 
    '''

    codon = CodonType()
    codon.Codon_Clasification()

    Gene = []
    for cod in Read_String(string):

        if cod.error:
            yield cod
            del(Gene[:])
            break
        
        else:
            if (cod.cod in codon.normal_codon):
                Gene.append(cod.cod)

            elif(cod.cod in codon.stop_codon):
                #If there are one or more elements in the Gene list then we found a complete gen, otherwise there is a sequence of stop codons
                if len(Gene) > 0:
                    Gene.append(cod.cod)
                    gen = Res('Gen', gen = Gene)
                    yield gen
                    del(Gene[:])
                else:
                    continue
            
            elif len(cod.cod) < 3:
                Error = Res('InvalidLength', error = True)
                yield Error
                del(Gene[:])
                break

    #If the last gen has not an stop codon, then there is an error        
    if len(Gene) > 0:
        Error = Res('UnexpectedEnd', error = True)
        yield Error


def Read_String(string):
    '''
    This function reads reads line by line the string and separates its codons.
    Whitespace characters are ignored. If there is a >, then goes to next line.
    The last group of elements is sended even there is no 3 elements.
    '''

    cod = ''

    for l, line in enumerate(string.splitlines()):
        for pos, el in enumerate(line):
            #Check if there is a whitespace. If yes ignore it and go to next character
            if re.match(r'\s', el):
                pos += 1
                continue
            #Check if there is a >. If yes ignore it and go to next line
            elif el == '>':
                break
            #Check if the is a A,U,C,G character. If yes add it to the cod string until its length is 3
            elif re.match('[AUCG]', el.upper()):
                cod = cod + el.upper()
                if(len(cod) == 3):
                    Codon = Res('Codon', cod)
                    cod = ''
                    yield Codon
            else:
                Error = Res('InvalidChar', error = True, error_atr = [l, pos])
                yield Error

    #If the last codon has 1 or 2 character, then the string has an invalid length
    if(cod != ''):
        Codon = Res('Codon', cod)
        yield Codon


if __name__ == '__main__':
    main()
