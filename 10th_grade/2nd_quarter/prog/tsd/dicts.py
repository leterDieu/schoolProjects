from __future__ import annotations
from collections.abc import Iterable


class Dict[K, V]:
    collection: Iterable[tuple[K, V]]

    def __init__(self, collection: Iterable[tuple[K, V]]) -> None:
        self.collection = set(collection)
        self.shadow_set = set(self.collection)
        self.keys = [i[0] for i in self.shadow_set]
        self.values = [i[1] for i in self.shadow_set]

    def __str__(self) -> str:
        return ', '.join([f'{key}: {value}' for key, value in self.shadow_set])

    def __in__(self, elem: V) -> bool:
        return elem in self.values

    def __contains__(self, elem: V) -> bool:
        return elem in self.values

    def __getitem__(self, key: K) -> V:
        if key not in self.keys:
            raise KeyError
        return list(self.values)[list(self.keys).index(key)]
