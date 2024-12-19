from trie import Trie
from avl_sets import AVLSet
from timeit import timeit
from typing import List
import json
import os
import random


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


with open(os.path.join(__location__, 'random_generated_strings.json'), 'r', encoding='utf-8') as f:
    random_generated_strings = json.loads(f.read())

with open(os.path.join(__location__, 'same_pref_generated_strings.json'), 'r', encoding='utf-8') as f:
    same_pref_generated_strings = json.loads(f.read())

with open(os.path.join(__location__, 'dif_pref_generated_strings.json'), 'r', encoding='utf-8') as f:
    dif_pref_generated_strings = json.loads(f.read())

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

trie_random = trie_adding(random_generated_strings)
set_random = avl_set_adding(random_generated_strings)

trie_same_pref = trie_adding(same_pref_generated_strings)
set_same_pref = avl_set_adding(same_pref_generated_strings)

trie_dif_pref = trie_adding(dif_pref_generated_strings)
set_dif_pref = avl_set_adding(dif_pref_generated_strings)


if __name__ == '__main__':
    print('trie speed (ms):', timeit(lambda: search_element_trie(trie_random, get_random_element(random_generated_strings)), number=10))
    print('set speed (ms):', timeit(lambda: search_element_avl_set(set_random, get_random_element(random_generated_strings)), number=10))

    print('same pref trie speed (ms):', timeit(lambda: search_element_trie(trie_same_pref, get_random_element(same_pref_generated_strings)), number=10))
    print('same pref set speed (ms):', timeit(lambda: search_element_avl_set(set_same_pref, get_random_element(same_pref_generated_strings)), number=10))

    print('dif pref trie speed (ms):', timeit(lambda: search_element_trie(trie_dif_pref, get_random_element(dif_pref_generated_strings)), number=10))
    print('dif pref set speed (ms):', timeit(lambda: search_element_avl_set(set_dif_pref, get_random_element(dif_pref_generated_strings)), number=10))
