from Add_Books import *
import unittest

class Testing(unittest.TestCase):

    def test_add(self):
        add = AddBooks()
        result = add.add_books1('bipino', 'rollon','11','erere','eregfd','reteet','uu')
        self.assertEqual(result, True)

    def test_add1(self):
        add = AddBooks()
        result = add.add_books1('bipino', '','12','erere','eregfd','reteet','uiopo')
        self.assertFalse(result)

    def test_delete(self):
        add =AddBooks()
        result = add.delete_item('')
        self.assertEqual(result,False)

    def test_delete2(self):
        add =AddBooks()
        result = add.delete_item('44')
        self.assertFalse(result)

    def test_update(self):
        add = AddBooks()
        result = add.update_item('','dd','fg','rr','ee','tt','yy','yo')
        self.assertFalse(result)

    def test_update1(self):
        add = AddBooks()
        result = add.update_books(44,'fg','rr','ee','','yy','yo','y')
        self.assertTrue(result)




