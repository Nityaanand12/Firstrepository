import unittest
from main_test import fun,Even_check

class fest(unittest.TestCase):
    def test_10_20(self):
        act= 0.5
        exp=fun(10,20)
        self.assertEqual(exp,act,'Test_10_20 is failed')
    def test_str2(self):
        act= None
        exp=fun('str2',20)
        self.assertEqual(exp,act,'Test_str2 is failed')
    def test_10_0(self):
        exp= None
        act=fun(10,0)
        self.assertEqual(exp,act,'Test_str3 is failed')
        
        
class Fest1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = 'zzzzzzzzzzz'
        print('started')
    @classmethod
    def tearDownClass(cls):
        print('completed')
    def setUp(self):
        print('create resoure')
    def tearDown(self):
        print('delete resoure')
    def test_even_10(self):
        act = 'Even'
        exp = Even_check(10)
        self.assertEqual(exp,act,'test_even_10 is failed')   
    def test_even_15(self):
        act = 'Odd'
        exp = Even_check(15)
        self.assertEqual(exp,act,'test_even_15 is failed')  
    def test_even_abce(self):
        act = None
        exp = Even_check('abce')
        self.assertEqual(exp,act,'test_even_abce is failed')  
    def test_even_empty(self):
        act = 'Even'
        exp = Even_check()
        self.assertEqual(exp,act,'test_even_empty is failed')
        
        
unittest.main()

