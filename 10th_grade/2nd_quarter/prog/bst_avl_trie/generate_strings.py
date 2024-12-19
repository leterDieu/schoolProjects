import itertools
import json
import os
import random


chars = 'abcd'
string_combs = [''.join(i) for i in itertools.product(chars, repeat=4)]


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'random_generated_strings.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(string_combs))

with open(os.path.join(__location__, 'same_pref_generated_strings.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(['a' * 1000 + el for el in string_combs]))

with open(os.path.join(__location__, 'dif_pref_generated_strings.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps([str(random.randint(1, 1000)) + el for el in string_combs]))
