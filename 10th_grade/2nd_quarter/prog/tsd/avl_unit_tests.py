import unittest
from typing import List

from avl_trees import AVLNode, AVLTree


def add_values(tree: AVLTree, values: List[int]) -> None:
    for value in values:
        tree.add(value)
    return None


def delete_valeus(tree: AVLTree, values: List[int]) -> None:
    for value in values:
        tree.delete(value)
    return None


class TestAVLTreeMethods(unittest.TestCase):
    def test_search_in_an_empty_tree(self):
        tree = AVLTree()
        self.assertIs(tree.search(1), None)

    def test_search_is_not_there(self):
        tree = AVLTree()
        add_values(tree, [1, 2, 4, 5, 2, 3])
        self.assertIs(tree.search(100), None)

    def test_search_is_there(self):
        tree = AVLTree()
        add_values(tree, [1, 2, 4, 5, 2, 3])
        self.assertEqual(tree.search(3), AVLNode(3))

    def test_add_to_an_empty_tree(self):
        tree = AVLTree()
        tree.add(1)
        expected_tree = AVLTree()
        expected_tree.root = AVLNode(1)
        self.assertEqual(tree, expected_tree)

    def test_add_greater_value_to_a_one_node_tree(self):
        tree = AVLTree()
        add_values(tree, [1, 2])
        expected_tree = AVLTree()
        expected_tree.add(1)
        expected_tree.root.right = AVLNode(2)
        self.assertEqual(tree, expected_tree)

    def test_add_smaller_value_to_a_one_node_tree(self):
        tree = AVLTree()
        add_values(tree, [1, -1])
        expected_tree = AVLTree()
        expected_tree.add(1)
        expected_tree.root.left = AVLNode(-1)
        self.assertEqual(tree, expected_tree)

    def test_add_smaller_value_than_left_no_right(self):
        tree = AVLTree()
        add_values(tree, [3, 2, 1])
        expected_tree = AVLTree()
        add_values(expected_tree, [2, 1, 3])
        self.assertEqual(tree, expected_tree)

    def test_add_greater_value_than_left_no_right(self):
        tree = AVLTree()
        add_values(tree, [3, 1, 2])
        expected_tree = AVLTree()
        add_values(expected_tree, [2, 1, 3])
        self.assertEqual(tree, expected_tree)

    def test_add_greater_value_than_right_no_left(self):
        tree = AVLTree()
        add_values(tree, [1, 2, 3])
        expected_tree = AVLTree()
        add_values(expected_tree, [2, 1, 3])
        self.assertEqual(tree, expected_tree)

    def test_add_smaller_value_than_right_no_left(self):
        tree = AVLTree()
        add_values(tree, [1, 3, 2])
        expected_tree = AVLTree()
        add_values(expected_tree, [2, 1, 3])
        self.assertEqual(tree, expected_tree)

    def test_to_list(self):
        tree = AVLTree()
        lst = [4, 2, 1, 4, 1, 3, 7, -1, 0, 32]
        add_values(tree, lst)
        expected_lst = [-1, 0, 1, 2, 3, 4, 7, 32]
        self.assertEqual(tree.to_list(), expected_lst)

    def test_to_list_empty(self):
        tree = AVLTree()
        expected_lst = []
        self.assertEqual(tree.to_list(), expected_lst)

    def test_merge_two_empty_trees(self):
        tree = AVLTree()
        other_tree = AVLTree()
        expected_tree = AVLTree()
        tree.merge(other_tree)
        self.assertEqual(tree, expected_tree)

    def test_merge_to_an_empty(self):
        tree = AVLTree()
        other_tree = AVLTree()
        lst = [-1, 3, 1, 2, 5]
        add_values(other_tree, lst)
        expected_tree = AVLTree()
        add_values(expected_tree, lst)
        tree.merge(other_tree)
        self.assertEqual(tree, expected_tree)

    def test_merge_an_empty(self):
        tree = AVLTree()
        other_tree = AVLTree()
        lst = [-1, 3, 1, 2, 5]
        add_values(tree, lst)
        expected_tree = AVLTree()
        add_values(expected_tree, lst)
        tree.merge(other_tree)
        self.assertEqual(tree, expected_tree)

    def test_merge(self):
        tree = AVLTree()
        other_tree = AVLTree()
        lst = [-1, 3, 1, 2, 5]
        other_lst = [7, -2, 12, 8, -4]
        add_values(tree, lst)
        add_values(other_tree, other_lst)
        expected_tree = AVLTree()
        add_values(expected_tree, lst)
        add_values(expected_tree, other_lst)
        tree.merge(other_tree)
        self.assertEqual(tree, expected_tree)

    def test_delete_unpresented(self):
        tree = AVLTree()
        add_values(tree, [1, 2])
        tree.delete(3)
        expected_tree = AVLTree()
        add_values(expected_tree, [1, 2])
        self.assertEqual(tree, expected_tree)

    def test_delete_from_empty(self):
        tree = AVLTree()
        tree.delete(1)
        expected_tree = AVLTree()
        self.assertEqual(tree, expected_tree)

    def test_delete_right_no_sub_tree(self):
        tree = AVLTree()
        add_values(tree, [1, 2])
        tree.delete(2)
        expected_tree = AVLTree()
        expected_tree.add(1)
        self.assertEqual(tree, expected_tree)

    def test_delete_left_no_sub_tree(self):
        tree = AVLTree()
        add_values(tree, [2, 1])
        tree.delete(1)
        expected_tree = AVLTree()
        expected_tree.add(2)
        self.assertEqual(tree, expected_tree)

    def test_delete_left_with_sub_trees(self):
        tree = AVLTree()
        add_values(tree, [1, 2, 3, 4, 5, 6, 7, 8])
        tree.delete(2)
        expected_tree = AVLTree()
        add_values(expected_tree, [4, 1, 3, 6, 5, 7, 8])
        self.assertEqual(tree, expected_tree)

    def test_delete_right_with_sub_trees(self):
        tree = AVLTree()
        add_values(tree, [1, 2, 3, 4, 5, 6, 7, 8])
        tree.delete(6)
        expected_tree = AVLTree()
        add_values(expected_tree, [4, 2, 1, 3, 5, 7, 8])
        self.assertEqual(tree, expected_tree)

    def test_delete_root_with_sub_trees(self):
        tree = AVLTree()
        add_values(tree, [1, 2, 3, 4, 5, 6, 7, 8])
        tree.delete(4)
        expected_tree = AVLTree()
        add_values(expected_tree, [1, 2, 3, 5, 6, 7, 8])
        self.assertEqual(tree, expected_tree)

    def delete_root_no_subtrees(self):
        tree = AVLTree()
        tree.add(1)
        tree.delete(1)
        expected_tree = AVLTree()
        self.assertEqual(tree, expected_tree)

    def delete_root_with_only_left_subtree(self):
        tree = AVLTree()
        add_values(tree, [2, 1])
        tree.delete(2)
        expected_tree = AVLTree()
        expected_tree.add(1)
        self.assertEqual(tree, expected_tree)

    def delete_root_with_only_right_subtree(self):
        tree = AVLTree()
        add_values(tree, [2, 3])
        tree.delete(2)
        expected_tree = AVLTree()
        expected_tree.add(3)
        self.assertEqual(tree, expected_tree)


if __name__ == '__main__':
    unittest.main()
