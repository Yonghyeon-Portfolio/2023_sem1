import unittest
from Node import Node
from DoublyLinkedList import DoublyLinkedList as DBLList

class Double_ll_test(unittest.TestCase):
    def test_instantiaion(self):
        dl = DBLList()
        self.assertEqual(dl.size(), 0)
    
    def test_insertion(self):
        dl = DBLList()
        dl.insert_before(None, Node(5))
        self.assertEqual(dl.last().get_value(), 5)
        
        dl.insert_after(dl.first(), Node(10))
        self.assertEqual(dl.first().get_value(), 5)
        self.assertEqual(dl.last().get_value(), 10)
        self.assertEqual(dl.size(), 2)
        
        dl.insert_before(None, Node(1)) # ignored
        self.assertEqual(dl.size(), 2)
        
        dl.insert_after(Node(2), Node(3)) # invalid (non-existenet node)
        self.assertEqual(dl.size(), 2)
    
    def test_invalid_insertion(self):
        dl = DBLList()
        dl.insert_before(Node(3), Node(5))
        self.assertEqual(dl.size(), 0)
        dl.insert_before(None, None)
        self.assertEqual(dl.size(), 0)

            
    def test_deletion(self):
        head, second, third = Node(10), Node(20), Node(30)
        dl = DBLList(head)
        dl.insert_after(head, third)
        dl.insert_before(third, second)
        self.assertEqual(dl.first().get_value(), 10)
        self.assertEqual(dl.last().get_value(), 30)
        
        dl.remove(second)
        self.assertEqual(dl.size(), 2)
        self.assertEqual(dl.first().get_value(), 10)
        self.assertEqual(dl.last().get_value(), 30)
        
        dl.remove(head)
        self.assertEqual(dl.size(), 1)
        self.assertEqual(dl.first().get_value(), 30)
        self.assertEqual(dl.last().get_value(), 30)
        
        dl.remove(third)
        self.assertEqual(dl.size(), 0)
        self.assertIsNone(dl.first())
        self.assertIsNone(dl.last())
        
        dl.remove(head)
        self.assertEqual(dl.size(), 0)
        self.assertIsNone(dl.first())
        self.assertIsNone(dl.last())
        
    

if __name__ == "__main__":
    unittest.main()