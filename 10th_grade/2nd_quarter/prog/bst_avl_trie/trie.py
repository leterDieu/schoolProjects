from __future__ import annotations
from avl_dicts import AVLDict
from typing import List


class TrieNode:
    value: AVLDict
    parent: None | TrieNode

    def __init__(self) -> None:
        self.value = AVLDict({})
        self.parent = None

    def __getitem__(self, code) -> None | TrieNode:
        return self.value[code]

    def __setitem__(self, code, value) -> None:
        if code in self.value.keys():
            return None

        self.value[code] = value

    def __delitem__(self, code) -> None:
        del self.value[code]

    @staticmethod
    def _prefix_match_(s1: str, s2: str) -> str:
        if s1[0] != s2[0]:
            return ''

        cut = 0
        for i, char in enumerate(s1):
            try:
                if char != s2[i]:
                    break
            except IndexError:
                    break
            cut = i
        return s1[:cut + 1]

    def _keys_(self) -> List[str]:
        return self.value.keys()

    def _find_max_prefix_info_(self, s: str) -> AVLDict[(str, str | None | AVLDict[(str, str)])]:
        max_prefix = ''
        max_prefix_key = None
        for key in self._keys_():
            current_prefix = self._prefix_match_(key, s)
            if len(max_prefix) < len(current_prefix):
                max_prefix = current_prefix
                max_prefix_key = key

        dct = AVLDict({})
        dct['key'] = max_prefix_key
        dct['prefix'] = max_prefix
        suffixes = AVLDict({})
        if max_prefix_key is not None:
            suffixes['main'] = max_prefix_key[len(max_prefix):]
        else:
            suffixes['main'] = ''
        suffixes['new'] = s[len(max_prefix):]
        dct['splits'] = suffixes
        return dct

    def _get_root_(self) -> TrieNode:
        if self.parent is None:
            return self
        return self.parent._get_root_()

    def _in_self_(self, s: str) -> bool:
        if s in self.value:
            return '\0' in self[s].value
        return False

    def add(self, s: str, push_parent: None | TrieNode = None) -> None:
        if not s:
            return None

        max_prefix_info = self._find_max_prefix_info_(s)

        if max_prefix_info['key'] == s:
            self[s]['\0'] = None
            return None

        if max_prefix_info['key'] == None:
            self[s] = TrieNode()
            self[s]['\0'] = None
            self.parent = push_parent
            return None

        if max_prefix_info['key'] == max_prefix_info['prefix']:
            self[max_prefix_info['prefix']].add(max_prefix_info['splits']['new'], self)
            return None

        self[max_prefix_info['prefix']] = TrieNode()
        self[max_prefix_info['prefix']].parent = self
        self[max_prefix_info['prefix']][max_prefix_info['splits']['main']] = self[max_prefix_info['key']]
        if max_prefix_info['splits']['new']:
            self[max_prefix_info['prefix']][max_prefix_info['splits']['new']] = TrieNode()
            self[max_prefix_info['prefix']][max_prefix_info['splits']['new']].parent = self
            self[max_prefix_info['prefix']][max_prefix_info['splits']['new']]['\0'] = None
        else:
            self[max_prefix_info['prefix']]['\0'] = None
        del self[max_prefix_info['key']]
        return None

    def __contains__(self, s: str) -> bool:
        if not s:
            return False

        if self._in_self_(s):
            return True

        max_prefix_info = self._find_max_prefix_info_(s)
        if max_prefix_info['key'] is None:
            return False

        return max_prefix_info['splits']['new'] in self[max_prefix_info['key']]

    def delete(self, s: str) -> None:
        if s not in self:
            return None

        max_prefix_info = self._find_max_prefix_info_(s)

        if max_prefix_info['key'] != s:
            self[max_prefix_info['prefix']].delete(max_prefix_info['splits']['new'])
            return None

        del self[s]['\0']

        if not self[s]._length_():
            del self[s]

        if self._length_() == 1 and self.parent is not None:
            append_string = self._find_single_()
            owner_string = self.parent._find_owner_(append_string)
            self.parent[owner_string + append_string] = self[append_string]
            del self.parent[owner_string]

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)

    def _length_(self) -> int:
        return self.value.length()

    def _find_single_(self) -> str | None:
        if self._length_() != 1:
            raise ValueError
            return None
        return self.value.tree.to_list()[0][0]

    def _find_owner_(self, s: str) -> str | None:
        for char in self.value.tree.to_list():
            if s in char[1]:
                return char[0]
        return None

    def to_list(self, prefix: str = '') -> List[str]:
        lst = []
        keys = self._keys_()

        if not len(keys):
            return None

        for key in keys:
            if self[key]:
                if '\0' in self[key]._keys_():
                    lst.append(prefix + key)
                lst.extend(self[key].to_list(prefix + key))

        return lst


class Trie:
    root: TrieNode | None

    def __init__(self) -> None:
        self.root = None

    def add(self, s: str) -> None:
        if self.root is not None:
            self.root.add(s)
            return None
        self.root = TrieNode()
        self.root[s] = TrieNode()
        self.root[s]['\0'] = None
        return None

    def __contains__(self, s: str) -> bool:
        if self.root is None:
            return False
        return s in self.root

    def delete(self, s: str) -> None:
        if self.root is None:
            return None
        self.root.delete(s)
        return None

    def __str__(self) -> str:
        return str(self.root)

    def __repr__(self) -> str:
        return str(self.root)

    def to_list(self) -> List[str]:
        if self.root is None:
            return []
        lst = self.root.to_list()
        if lst is None:
            return []
        return lst
