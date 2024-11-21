from __future__ import annotations
from collections.abc import Iterable
from enum import Enum, auto
from trees import Node, Tree, Compare


class Dict[K, V]:
    tree: Tree[tuple[K, V]]

    @staticmethod
    def _compare_(item_1: tuple[K, V], item_2: tuple[K, V]) -> Compare:
        if item_1[1] < item_2[1]:
            return Compare.Less
        elif item_1[1] == item_2[1]:
            return Compare.Equal
        return Compare.Greater

    def __init__(self, collection: Iterable[tuple[K, V]]) -> None:
        iter = collection.__iter__()
        try:
            first_item, *rest_of_items = iter
            start_node = Node(first_item, Dict._compare_)
            for i in rest_of_items:
                start_node.add(Node(i))
            self.tree = Tree(start_node)
        except ValueError:
            t_node = Node((0, 0), Dict._compare_)
            self.tree = Tree(t_node)
            self.tree.delete(t_node)
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
        t_node = self.tree.search(Node((code, self[code]), Dict._compare_))
        self.tree.delete(t_node)
