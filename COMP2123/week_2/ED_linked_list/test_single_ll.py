import unittest
from single_ll import Single_ll
from Node import Node

class LkList_Test(unittest.TestCase):
    def test_initialisation(self):
        head = Node(5)
        lk_list = Single_ll(head)
        self.assertIs(lk_list.first(), lk_list.last())
        self.assertEqual(lk_list.first().get_value(), 5)
        self.assertIsNone(lk_list.last().get_next(), None)
    
    def test_insert_after(self):
        head, second, third = Node(1), Node(2), Node(3)
        lk_list = Single_ll(head)
        lk_list.insert_after(head, second)
        lk_list.insert_after(second, third)
        self.assertIs(lk_list.first(), head)
        self.assertIs(lk_list.last(), third)

        lk_list.insert_after(None, Node(4))
        self.assertEqual(lk_list.first().get_value(), 4)
        self.assertEqual(lk_list.last().get_value(), 3)
        self.assertEqual(lk_list.size(), 4)

    def test_remove_node(self):
        lk_list = Single_ll(Node(1))
        lk_list.insert_after(lk_list.last(), Node(2))
        lk_list.insert_after(lk_list.last(), Node(3))
        lk_list.insert_after(lk_list.last(), Node(4))
        lk_list.insert_after(lk_list.last(), Node(5))

        # remove first element
        r = lk_list.remove(lk_list.first())
        self.assertEqual(r.get_value(), 1)
        self.assertEqual(lk_list.first().get_value(), 2)
        self.assertEqual(lk_list.size(), 4)
        # remove last element 
        r = lk_list.remove(lk_list.last())
        self.assertEqual(r.get_value(), 5)
        self.assertEqual(lk_list.last().get_value(), 4)
        self.assertEqual(lk_list.size(), 3)
        # remove middle element
        six = Node(6)
        seven = Node(7)
        lk_list.insert_after(lk_list.last(), six)
        lk_list.insert_after(lk_list.last(), seven)
        self.assertEqual(lk_list.last().get_value(), 7)
        self.assertEqual(lk_list.size(), 5)
        r = lk_list.remove(six)
        self.assertEqual(r.get_value(), 6)
        self.assertEqual(lk_list.last().get_value(), 7)
        self.assertEqual(lk_list.size(), 4)
        # remove non-existent element
        r = lk_list.remove(Node(3)) # different object, so non-existenet
        self.assertIsNone(r)
        self.assertEqual(lk_list.size(), 4)
        # remove None 
        r = lk_list.remove(None)
        self.assertIsNone(r)
        self.assertEqual(lk_list.size(), 4)
    
    def test_remove_from_empty(self):
        lk_list = Single_ll(Node(5))
        r = lk_list.remove(lk_list.first())
        self.assertIsNone(lk_list.first())
        self.assertIsNone(lk_list.last())
        self.assertEqual(lk_list.size(), 0)
        r = lk_list.remove(lk_list.last())
        self.assertIsNone(r)
        self.assertEqual(lk_list.size(), 0)

if __name__ == "__main__":
    unittest.main()