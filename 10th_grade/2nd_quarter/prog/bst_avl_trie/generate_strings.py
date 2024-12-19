import itertools
import json
import os


chars = 'abcd'
string_combs = [''.join(i) for i in itertools.product(chars, repeat=4)]


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'generated_strings.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(string_combs))
