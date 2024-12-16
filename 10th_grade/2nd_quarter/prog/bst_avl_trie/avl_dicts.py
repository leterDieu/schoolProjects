from __future__ import annotations
from collections.abc import Iterable
from avl_trees import AVLTree, Compare
from typing import List


class AVLDict[K, V]:
    tree: AVLTree[tuple[K, V]]

    @staticmethod
    def _compare_(item_1: tuple[K, V], item_2: tuple[K, V]) -> Compare:
        if item_1[1] < item_2[1]:
            return Compare.Less
        elif item_1[1] == item_2[1]:
            return Compare.Equal
        return Compare.Greater

    def __init__(self, collection: Iterable[tuple[K, V]]) -> None:
        iter = collection.__iter__()
        self.tree = AVLTree()
        try:
            first_item, *rest_of_items = iter
            self.tree.add(first_item)
            for i in rest_of_items:
                self.tree.add(i)
        except ValueError:
            pass
        return None

    def __str__(self) -> str:
        return str(self.tree.to_list())

    def __repr__(self) -> str:
        return str(self.tree.to_list())

    def __in__(self, key: K) -> bool:
        return key in [i[0] for i in self.tree.to_list()]

    def __contains__(self, key: K) -> bool:
        return key in [i[0] for i in self.tree.to_list()]

    def __getitem__(self, key: K) -> V | None:
        for i in self.tree.to_list():
            if i[0] == key:
                return i[1]
        raise KeyError
        return None

    def __delitem__(self, code) -> None:
        if code not in self:
            return None
        self.tree.delete((code, self[code]))

    def __setitem__(self, code, value) -> None:
        if code in self:
            return None

        self.tree.add((code, value))

    def keys(self) -> List[K]:
        return [el[0] for el in self.tree.to_list()]

    def length(self) -> int:
        return len(self.tree.to_list())
