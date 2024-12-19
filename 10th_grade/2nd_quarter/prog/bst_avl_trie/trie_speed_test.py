from trie import Trie
from avl_sets import AVLSet
from timeit import timeit
from typing import List
import json
import os
import random


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


with open(os.path.join(__location__, 'generated_strings.json'), 'r', encoding='utf-8') as f:
    generated_strings = json.loads(f.read())

def trie_adding(strings: List[str]) -> Trie:
    trie_eq_prefixes = Trie()
    for s in strings:
        trie_eq_prefixes.add(s)
    return trie_eq_prefixes

def avl_set_adding(strings: List[str]) -> AVLSet[str]:
    set_eq_prefixes = AVLSet({})
    for s in strings:
        set_eq_prefixes.add(s)
    return set_eq_prefixes


def get_random_element(given_strings: List[str]) -> str:
    random_element = random.choice(given_strings)
    if random.randint(0, 1):
        random_element += 'x'
    return random_element

def search_element_trie(given_trie: Trie, random_element: str) -> bool:
    return random_element in given_trie

def search_element_avl_set(given_avl_set: AVLSet[str], random_element: str) -> bool:
    return random_element in given_avl_set

trie_full = trie_adding(generated_strings)
set_full = avl_set_adding(generated_strings)


if __name__ == '__main__':
    print('trie speed (ms):', timeit(lambda: search_element_avl_set(set_full, get_random_element(generated_strings)), number=10))
    print('set speed (ms):', timeit(lambda: search_element_trie(trie_full, get_random_element(generated_strings)), number=10))
