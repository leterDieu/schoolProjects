from trie import Trie
import tracemalloc

prefix = 'qwertyuiopasdfghjklzxcvbnm'
strings_eq_prefixes = [
    prefix + 'a',
    prefix + 'b',
    prefix + 'c'
]

tracemalloc.start()

set_eq_prefixes = set()
for s in strings_eq_prefixes:
    set_eq_prefixes.add(s)

print('set_eq_prefixes:', tracemalloc.get_traced_memory())

tracemalloc.clear_traces()

trie_eq_prefixes = Trie()
for s in strings_eq_prefixes:
    trie_eq_prefixes.add(s)

print('trie_eq_prefixes:', tracemalloc.get_traced_memory())
