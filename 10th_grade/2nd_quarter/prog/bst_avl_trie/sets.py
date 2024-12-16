from __future__ import annotations
from collections.abc import Iterable
from trees import Node, Tree, Compare

class Set[T]:
    tree: Tree[T]

    @staticmethod
    def _compare_(item_1: T, item_2: T) -> Compare:
        if item_1 < item_2:
            return Compare.Less
        elif item_1 == item_2:
            return Compare.Equal
        return Compare.Greater

    def __init__(self, collection: Iterable[T]) -> None:
        iter = collection.__iter__()
        try:
            first_item, *rest_of_items = iter
            start_node = Node(first_item, Set._compare_)
            for i in rest_of_items:
                start_node.add(i)
            self.tree = Tree(start_node)
        except ValueError:
            self.tree = Tree()
        return None

    def __str__(self) -> str:
        return str(self.tree.to_list())

    def __repr__(self) -> str:
        return str(self.tree.to_list())

    def add(self, value: T) -> None:
        self.tree.add(value)
        return None

    def delete(self, value: T) -> None:
        self.tree.delete(value)
        return None

    def __and__(self, other: Set[T]) -> Set[T]:
        lst = []
        for i in self.tree.to_list():
            if other.tree.search(i) is not None:
                lst.append(i)
        return Set(lst)

    def __or__(self, other: Set[T]) -> Set[T]:
        lst = []
        for i in self.tree.to_list():
            lst.append(i)
        for i in other.tree.to_list():
            lst.append(i)

        return Set(lst)

    def is_subset(self, other: Set[T]) -> bool:
        other_lst = other.tree.to_list()
        for i in self.tree.to_list():
            if i not in other_lst:
                return False
        return True

    def is_empty(self) -> bool:
        return not len(self.tree.to_list())
