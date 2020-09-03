from Application import *
import unittest

class Testing(unittest.TestCase):

    def test_login(self):
        login = Guis()
        result = login.do_login('bipino', 'rollon')
        self.assertEqual((len(result)),1)

    def test_login1(self):
        login = Guis()
        result = login.do_login('bipjho', 'exvjhp')
        self.assertEqual((len(result)),0)

    def test_add(self):
        login = Guis()
        result = login.do_register('simon', 'exporer','BipinDhakal','Thankt','980778743','bipin7@gmail.com')
        self.assertTrue(result)

    def test_add1(self):
        login = Guis()
        result = login.do_register('bipino', 'explrer','','Thnkot','980678743','bipin7@gmail.com')
        self.assertFalse(result)


    

