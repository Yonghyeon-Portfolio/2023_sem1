import unittest
import sys

from Node import Node

class NodeTest(unittest.TestCase):
    def test_initialisation(self):
        sample_head = Node(5, None)
        second_node = Node(10, None)
        self.assertIsNone(sample_head.get_next())
        sample_head.set_next(second_node)
        self.assertIs(sample_head.get_next(), second_node)
    
    def test_setting_vals(self):
        nodeA = Node(1, None)
        nodeB = Node(2, None)
        nodeC = Node(3, None)
        nodeD = Node(0, None)

        nodeA.set_next(nodeB)
        nodeB.set_next(nodeC)
        nodeD.set_next(nodeA)

        curr = nodeD
        for i in range(0, 4):
            self.assertEqual(curr.get_value(), i)
            curr.set_value(1000)
            curr = curr.get_next()
        
        curr = nodeD
        for i in range(0, 4):
            self.assertEqual(curr.get_value(), 1000)

if __name__ == "__main__":
    unittest.main()