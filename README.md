# Processing mRNA Sequence

## Challenge

This is a possible solution for the Code Challenge. This one is written in Python. This program reads a string or a file that contains a string as input. The input string is a sequence of mRNA which may contain whitespace characters (space, tab, linefeed, Unicode whitespace) that are ignored. The string may also contain comments prefixed with “>” (greater than) character. All data after that character until the end of the line is ignored.

Apart from whitespace and comments, the string should only contain the four characters A, U, G and C which may appear in upper or lowercase representation. If there is any other character in the string, the function returns an error state, indicating invalid character. 

The input string contains none, one or more genes. A gene is a sequence of codons terminated by a single stop codon. More stop codons are treated as noise and are ignored. A codon is a combination of three nucleotides (there are four possible nucleotides represented as A, U, G and C) and hence there is 64 possible codons. There are three are stop codons: UAG, UGA and UAA. A sequence of codons can be as follows: ... CUG UCU AUG GGA AAA UGC UGA UUA AGU UUU AUG UCC UCC ...

The function process the string character by character from the first position. 

The function returns a list where each item represents a gene. Each gene is a list where each element is a codon. Alternatively, the functions returns an error state, indicating invalid input. The errors are clasified as invalid character, invalid length (if the last codon has only one or two letters) and unexpected end (no stop codon at the end of the string).

## Installation Python

This projects needs Python in order to be compiled and run successfully. You can download it here: https://www.python.org/downloads/

## Compile and Run

We can pass a single file or a string as input. If we run:

```
python Challenge.py data\'refMrna.fa.txt'
```

Then the program prints a list of genes or an error.


