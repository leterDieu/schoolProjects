from __future__ import annotations
from collections.abc import Iterable

class Set[T]:
    collection: Iterable[T]

    def __init__(self, collection: Iterable[T]) -> None:
        self.collection = set(collection)
        self.shadow_set = set(self.collection)
        return None

    def __str__(self) -> str:
        return ' '.join([str(i) for i in self.collection])

    def add(self, elem: T) -> None:
        self.shadow_set.add(elem)
        self.collection = self.shadow_set
        return None

    def __in__(self, elem: T) -> bool:
        return elem in self.shadow_set

    def __contains__(self, elem: T) -> bool:
        return elem in self.shadow_set

    def delete(self, elem: T) -> None:
        if elem not in self.collection:
            return None
        self.shadow_set.remove(elem)
        self.collection = self.shadow_set

    def __and__(self, other: Set[T]) -> Set[T]:
        new_set = Set({})
        for i in self.collection:
            if i in other.collection:
                new_set.add(i)
        return new_set

    def __or__(self, other: Set[T]) -> Set[T]:
        new_set = self
        for i in other.collection:
            new_set.add(i)
        return new_set

    def is_subset(self, other: Set[T]) -> bool:
        for i in self.collection:
            if i not in other.collection:
                return False
        return True

    def is_empty(self) -> bool:
        return not bool(len(self.shadow_set))

    def __getitem__(self, key: int) -> T:
        return list(self.shadow_set)[key]
