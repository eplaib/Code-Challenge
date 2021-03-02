import unittest
import Challenge2

class TestChallenge(unittest.TestCase):

    def setUp(self):
        self.test1 = 'ugc auc     uag'.splitlines()
        self.test2 = 'ugc auc uac'.splitlines()
        self.UnexpecedEnd = 'Unexpected end of gene. The last gen has not stop codon at the end of the string'
        self.test3 = 'ugc juc uag'.splitlines()
        self.InvalidChar = 'Invalid characteres. There is an invalid character in line {0} position {1}'.format(0, 4)
        self.test4 = 'ugc auc ua'.splitlines()
        self.InvalidLength = 'Invalid string length. The last gen has not a valid string length. Each codon should have 3 nucleotides'
        self.test5 = '''ugc auc 
        >NM_001293063 1
        uag'''.splitlines()
        self.test6 = '''ugc auc >NM_001293063 1
        uag'''.splitlines()


    def test_gene_creation(self):
        for res1 in Challenge2.Gene_Creation(self.test1):
            self.assertEqual(res1,  ['UGC', 'AUC', 'UAG'])
        for res2 in Challenge2.Gene_Creation(self.test2):
            self.assertEqual(res2,  self.UnexpecedEnd)
        for res3 in Challenge2.Gene_Creation(self.test3):
            self.assertEqual(res3,  self.InvalidChar)
        for res4 in Challenge2.Gene_Creation(self.test4):
            print(res4)
            self.assertEqual(res4,  self.InvalidLength)
        for res5 in Challenge2.Gene_Creation(self.test5):
            self.assertEqual(res5,  ['UGC', 'AUC', 'UAG'])
        for res6 in Challenge2.Gene_Creation(self.test6):
            self.assertEqual(res6,  ['UGC', 'AUC', 'UAG'])

if __name__ == '__main__':
    unittest.main()
