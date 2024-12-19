import tracemalloc
from trie_speed_test import trie_adding, avl_set_adding, random_generated_strings, same_pref_generated_strings, dif_pref_generated_strings


tracemalloc.start()

trie_random = trie_adding(random_generated_strings)
print('trie mem: ', tracemalloc.get_traced_memory())
tracemalloc.clear_traces()

set_random = avl_set_adding(random_generated_strings)
print('set mem: ', tracemalloc.get_traced_memory())
tracemalloc.clear_traces()

trie_same_pref = trie_adding(same_pref_generated_strings)
print('trie mem same pref: ', tracemalloc.get_traced_memory())
tracemalloc.clear_traces()

set_same_pref = avl_set_adding(same_pref_generated_strings)
print('set mem same pref: ', tracemalloc.get_traced_memory())
tracemalloc.clear_traces()

trie_dif_pref = trie_adding(dif_pref_generated_strings)
print('trie mem dif pref: ', tracemalloc.get_traced_memory())
tracemalloc.clear_traces()

set_dif_pref = avl_set_adding(dif_pref_generated_strings)
print('set mem dif pref: ', tracemalloc.get_traced_memory())
tracemalloc.clear_traces()
