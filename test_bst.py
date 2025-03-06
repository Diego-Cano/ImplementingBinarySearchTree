import unittest
from bst_implementation import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        for value in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(value)

    def test_insertion(self):
        self.bst.insert(25)
        self.assertIn(25, self.bst.inorder_traversal())

    def test_insert_duplicate(self):
        self.bst.insert(30)  # 30 is already in the tree
        inorder_result = self.bst.inorder_traversal()
        self.assertEqual(inorder_result.count(30), 1)  # 30 should appear only once

    def test_search(self):
        self.assertIsNotNone(self.bst.search(30))
        self.assertIsNone(self.bst.search(100))

    def test_deletion_leaf(self):
        self.bst.delete(20)
        self.assertNotIn(20, self.bst.inorder_traversal())

    def test_deletion_one_child(self):
        self.bst.delete(30)
        self.assertNotIn(30, self.bst.inorder_traversal())

    def test_deletion_two_children(self):
        self.bst.delete(50)
        self.assertNotIn(50, self.bst.inorder_traversal())

    def test_delete_non_existent(self):
        initial_traversal = self.bst.inorder_traversal()
        self.bst.delete(100)  # 100 is not in the tree
        self.assertEqual(self.bst.inorder_traversal(), initial_traversal)  # Should remain unchanged

if __name__ == '__main__':
    unittest.main()
