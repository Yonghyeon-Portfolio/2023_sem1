from Node import Node
from Tree import Tree

import unittest


def assert_equal(got, expected, msg):
    """
    Simple assert helper
    """
    assert expected == got, "[{}] Expected: {}, got: {}".format(msg, expected, got)


class SampleTreeTestCases(unittest.TestCase):
    """
    Testing functionality of the Tree class
    """

    def setUp(self):
        """
        Set up the tree to be used throughout the test
        This is the tree given in the sample
                        (1)
                    /    |    \
                  (3)   (2)   (4)
                       /    \
                     (5)    (6)
        """

        self.tree = Tree()
        self.root = self.tree.add_child(None)
        self.A = self.tree.add_child(self.root)
        self.B = self.tree.add_child(self.root)
        self.C = self.tree.add_child(self.root)
        self.D = self.tree.add_child(self.A)
        self.E = self.tree.add_child(self.A)

    def test_construction(self):
        """
        Test that the sample tree has been correctly constructed
        """
        assert_equal(self.root.get_parent(), None, "Root has no parent")
        assert_equal(self.A.get_parent(), self.root, "A's parent is root")
        assert_equal(self.B.get_parent(), self.root, "B's parent is root")
        assert_equal(self.C.get_parent(), self.root, "C's parent is root")
        assert_equal(self.D.get_parent(), self.A, "D's parent is A")
        assert_equal(self.E.get_parent(), self.A, "E's parent is A")

    def test_min_pre_order_rank(self):
        """
        Test that the min preorder rank is successfully calculated
        """
        assert_equal(
            self.tree.min_pre_order_rank(self.root),
            1,
            "Root has min preorder rank of 1",
        )
        assert_equal(
            self.tree.min_pre_order_rank(self.D),
            3,
            "Node 5 has min preorder rank of 3",
        )
        self.assertEqual(self.tree.min_pre_order_rank(self.A), 2)
        self.assertEqual(self.tree.min_pre_order_rank(self.B), 2)
        self.assertEqual(self.tree.min_pre_order_rank(self.C), 2)
        self.assertEqual(self.tree.min_pre_order_rank(self.D), 3)
        self.assertEqual(self.tree.min_pre_order_rank(self.E), 3)

    def test_attach(self):
        """
        Test that the attach function works as intended
        """

        # Form a new tree
        tree = Tree()
        A = tree.add_child(None)
        # tree.root = A
        B = tree.add_child(A)
        C = tree.add_child(A)
        D = tree.add_child(B)

        # Attach the new tree to the root of the sample tree
        self.tree.attach(tree, self.root)

        # Assert the nodes are properly attached
        assert_equal(A.get_parent(), self.root, "A's parent is root")
        assert_equal(B.get_parent(), A, "B's parent is A")
        assert_equal(C.get_parent(), A, "C's parent is A")
        assert_equal(D.get_parent(), B, "D's parent is B")
        assert_equal(A in self.root.get_children(), True, "Root has A as a child")

    def test_preorder(self):
        """
        Test that the preorder is successfully calculated
        """
        assert_equal(
            self.tree.pre_order([5, 2, 3, 6, 4, 1]),
            [self.root, self.A, self.D, self.E, self.B, self.C],
            "Incorrect preorder given for the sample tree",
        )
        assert_equal(
            self.tree.pre_order([6, 4, 3, 1, 2, 5]),
            [self.root, self.C, self.B, self.A, self.E, self.D],
            "Incorrect preorder given for the sample tree",
        )

if __name__ == "__main__":
    unittest.main()