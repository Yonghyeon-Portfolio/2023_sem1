from Node import Node
import unittest

class NodeTest(unittest.TestCase):
    def test_instantiation(self):
        Nd = Node(5)
        self.assertIsNotNone(Nd)
        self.assertEqual(Nd.ID, 5)
        self.assertIsNone(Nd.parent)
        self.assertEqual(len(Nd.children), 0)
    
    def test_children(self):
        NodeA = Node(5)
        # valid children
        A_child1, A_child2 = Node(10), Node(1)
        NodeA.add_child(A_child1)
        NodeA.add_child(A_child2)
        self.assertEqual(len(NodeA.get_children()), 2)
        # invalid children
        NodeA.add_child(None)
        NodeA.add_child(100)
        self.assertEqual(len(NodeA.get_children()), 2)
        
    def test_parent(self):
        Root = Node(10)
        child = Node(1)
        child.set_parent(Root)
        self.assertIs(child.get_parent(), Root)
        self.assertIs(Root.get_children()[0], child)
        
        # remove children by child's parent to None
        child.set_parent(None)
        self.assertIsNone(child.get_parent())
        self.assertEqual(len(Root.get_children()), 0)
    
    def test_print(self):
        Root = Node(10)
        child = Node(1)
        Root.add_child(child)
        Root.add_child(Node(2))
        print(Root)
        print(child)
        print(Root.get_children()[1])
    
if __name__ == "__main__":
    unittest.main()