import unittest
from typing import List

from avl_sets import AVLSet
from trie import Trie


def add_values(trie_or_avl_set: Trie | AVLSet, values: List[str]) -> None:
    for value in values:
        trie_or_avl_set.add(value)

class TestTrieMethods(unittest.TestCase):
    def test_search_in_an_empty_trie(self):
        trie = Trie()
        self.assertIs('a' in trie, False)

    def test_add_empty_string(self):
        trie = Trie()
        add_values(trie, [''])
        expected = AVLSet({})
        add_values(expected, [''])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_add_to_an_empty(self):
        trie = Trie()
        trie.add('a')
        expected = AVLSet({})
        expected.add('a')
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_add_extends(self):
        trie = Trie()
        add_values(trie, ['a', 'ab'])
        expected = AVLSet({})
        add_values(expected, ['a', 'ab'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_add_cuts_left(self):
        trie = Trie()
        add_values(trie, ['ab', 'a'])
        expected = AVLSet({})
        add_values(expected, ['ab', 'a'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_add_cuts_right(self):
        trie = Trie()
        add_values(trie, ['ab', 'b'])
        expected = AVLSet({})
        add_values(expected, ['ab', 'b'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_add_same_size_same_prefix(self):
        trie = Trie()
        add_values(trie, ['ab', 'ac'])
        expected = AVLSet({})
        add_values(expected, ['ab', 'ac'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_add_same_size_same_prefix_and_cut_left(self):
        trie = Trie()
        add_values(trie, ['ab', 'ac', 'a'])
        expected = AVLSet({})
        add_values(expected, ['ab', 'ac', 'a'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_add_diff(self):
        trie = Trie()
        add_values(trie, ['ab', 'bc'])
        expected = AVLSet({})
        add_values(expected, ['ab', 'bc'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_search_not_there(self):
        trie = Trie()
        add_values(trie, ['ab', 'b'])
        expected = AVLSet({})
        add_values(expected, ['ab', 'b'])
        self.assertEqual('a' in trie, 'a' in expected)

    def test_search_there(self):
        trie = Trie()
        add_values(trie, ['ab', 'b'])
        expected = AVLSet({})
        add_values(expected, ['ab', 'b'])
        self.assertEqual('ab' in trie, 'ab' in expected)

    def test_delete_from_empty(self):
        trie = Trie()
        trie.delete('a')
        expected = AVLSet({})
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_delete_with_only_one(self):
        trie = Trie()
        trie.add('a')
        trie.delete('a')
        expected = AVLSet({})
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_delete_with_two_on_the_same_level(self):
        trie = Trie()
        add_values(trie, ['a', 'b'])
        trie.delete('a')
        expected = AVLSet({})
        add_values(expected, ['b'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_delete_higher_highset(self):
        trie = Trie()
        add_values(trie, ['ab', 'b'])
        trie.delete('ab')
        expected = AVLSet({})
        add_values(expected, ['b'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_delete_lower_subset(self):
        trie = Trie()
        add_values(trie, ['ab', 'b'])
        trie.delete('b')
        expected = AVLSet({})
        add_values(expected, ['ab'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_delete_higher_not_highset(self):
        trie = Trie()
        add_values(trie, ['ab', 'a'])
        trie.delete('a')
        expected = AVLSet({})
        add_values(expected, ['ab'])
        self.assertEqual(trie.to_list(), expected.to_list())

    def test_delete_compress_inbetween(self):
        trie = Trie()
        add_values(trie, ['a', 'ab', 'abc'])
        trie.delete('ab')
        expected = AVLSet({})
        add_values(expected, ['a', 'abc'])
        self.assertEqual(trie.to_list(), expected.to_list())


if __name__ == '__main__':
    unittest.main()
