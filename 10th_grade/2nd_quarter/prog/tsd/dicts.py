from __future__ import annotations
from collections.abc import Iterable
from sets import Set

class Dict[T]:
    collection: Iterable[T]

    def __init__(self, collection: Iterable[Set[T]]) -> None:
        try:
            self.keys = set([i[0] for i in collection])
            self.values = set([i[1] for i in collection])
        except IndexError:
            # perhaps one should add a logger here
            pass
        return None

    def __str__(self) -> str:
        return ', '.join([f'{key}: {value}' for key, value in zip(self.keys, self.values)])

    def __in__(self, elem: T) -> bool:
        return elem in self.values

    def __contains__(self, elem: T) -> bool:
        return elem in self.values

    def __getitem__(self, key: T) -> T | None:
        if key not in self.keys:
            return None
        return list(self.values)[list(self.keys).index(key)]
