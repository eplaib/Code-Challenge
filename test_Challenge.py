import unittest
from Challenge import Genes_List
from Classes.results import Res

class TestChallenge(unittest.TestCase):

    def setUp(self):
        self.test1 = 'ugc auc     uag'
        self.test2 = 'ugc auc uac'
        self.UnexpecedEnd = Res('UnexpectedEnd', error=True)
        self.test3 = 'ugc juc uag'
        self.InvalidChar = Res('InvalidChar', error=True, error_atr = [0, 4])
        self.test4 = 'ugc auc ua'
        self.InvalidLength = Res('InvalidLength', error=True)
        self.test5 = '''ugcaucuag aaa uca 
        uga'''
        self.test6 = '''ugc auc 
        >NM_001293063 1
        uag'''
        self.test7 = '''ugc auc >NM_001293063 1
        uag'''

        

    def test_genes_list(self):
        
        self.assertEqual(Genes_List(self.test1),  [['UGC', 'AUC', 'UAG']])
        self.assertEqual(Genes_List(self.test2),  self.UnexpecedEnd._UnexpectedEnd())
        self.assertEqual(Genes_List(self.test3),  self.InvalidChar._InvalidChar())
        self.assertEqual(Genes_List(self.test4),  self.InvalidLength._InvalidLength())
        self.assertEqual(Genes_List(self.test5),  [['UGC', 'AUC', 'UAG'], ['AAA', 'UCA', 'UGA']])
        self.assertEqual(Genes_List(self.test6),  [['UGC', 'AUC', 'UAG']])
        self.assertEqual(Genes_List(self.test7),  [['UGC', 'AUC', 'UAG']])


if __name__ == '__main__':
    unittest.main()