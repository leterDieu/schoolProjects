from __future__ import annotations
from typing import Callable, List
from enum import Enum, auto


class Compare(Enum):
    Less = auto()
    Equal = auto()
    Greater = auto()


class Node[T]:
    value: T
    predicate: Callable[[T, T], Compare]
    left: Node[T] | None
    right: Node[T] | None
    parent: Node[T] | None
    char_length: int
    max_char_length: int

    def __init__(
            self,
            value: T,
            predicate: Callable[[T, T], Compare] = lambda first, second: (
                Compare.Less
                if first < second
                else (Compare.Greater if first > second else Compare.Equal)
            ),
        ) -> None:
            self.value = value
            self.predicate = predicate
            self.left = None
            self.right = None
            self.parent = None
            self.char_length = len(str(value))
            self.max_char_length = self.char_length

    def correct(self) -> bool:
        if self.left is not None:
            if not self.left.correct():
                return False
            if not self.predicate(self.left.value, self.value) == Compare.Less:
                return False
        if self.right is not None:
            if not self.right.correct():
                return False
            if not self.predicate(self.value, self.right.value) == Compare.Less:
                return False
        return True

    def search(self, value: T) -> Node[T] | None:
        if self.predicate(self.value, value) == Compare.Equal:
            return self
        if self.predicate(value, self.value) == Compare.Less:
            if self.left is not None:
                return self.left.search(value)
        if self.predicate(value, self.value) == Compare.Greater:
            if self.right is not None:
                return self.right.search(value)
        return None

    def get_root(self) -> Node[T]:
        if self.parent is None:
            return self
        return self.parent.get_root()

    # apply only for the root
    def change_max_char_length(self, length_value: int) -> None:
        self.max_char_length = length_value
        if self.left is not None:
            self.left.change_max_char_length(length_value)
        if self.right is not None:
            self.right.change_max_char_length(length_value)

    # apply only for the root
    def find_max_char_length(self) -> int:
        own_char_length, left_char_length, right_char_length = self.char_length, 0, 0
        if self.left is not None:
            left_char_length = self.left.find_max_char_length()
        if self.right is not None:
            right_char_length = self.right.find_max_char_length()
        return max(own_char_length, left_char_length, right_char_length)

    def add(self, value: T) -> None:
        if self.predicate(value, self.value) == Compare.Less:
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = Node(value)
                self.left.parent = self
                self.left.predicate = self.predicate

                if self.left.max_char_length > self.max_char_length:
                    self.get_root().change_max_char_length(self.left.max_char_length)
                else:
                    self.left.max_char_length = self.max_char_length

        if self.predicate(value, self.value) == Compare.Greater:
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = Node(value)
                self.right.parent = self
                self.right.predicate = self.predicate

                if self.right.max_char_length > self.max_char_length:
                    self.get_root().change_max_char_length(self.right.max_char_length)
                else:
                    self.right.max_char_length = self.max_char_length

    def most_right(self) -> Node[T]:
        if self.right is not None:
            return self.right.most_right()
        return self

    def is_right(self) -> bool | None:
        if self.parent is not None:
            return self.predicate(self.value, self.parent.value) == Compare.Greater
        return None

    def is_left(self) -> bool | None:
        is_right_return = self.is_right()
        if is_right_return is not None:
            return not is_right_return
        return None

    def clean(self) -> None:
        self.parent = None
        self.left = None
        self.right = None

    def delete(self, value: T) -> None:
        delete_item = self.search(value)
        if delete_item is None:
            return None

        if delete_item.parent is None:
            if delete_item.left is not None:
                delete_item.left.parent = None
                prev_most_right = delete_item.left.most_right()
                prev_most_right.right = delete_item.right
                if prev_most_right.right is not None:
                    prev_most_right.right.parent = prev_most_right
                # delete_item.clean()
                return None
            if delete_item.right is not None:
                delete_item.right.parent = None
            # delete_item.clean()
            return None

        if delete_item.is_left():
            if delete_item.left is not None:
                delete_item.parent.left = delete_item.left
                delete_item.left.parent = delete_item.parent
                prev_most_right = delete_item.left.most_right()
                prev_most_right.right = delete_item.right
                if prev_most_right.right is not None:
                    prev_most_right.right.parent = prev_most_right
                return None
            if delete_item.right is not None:
                delete_item.parent.left = delete_item.right
                delete_item.right.parent = delete_item.parent
                return None
            delete_item.parent.left = None
            # delete_item.clean()
            return None

        if delete_item.left is not None:
            delete_item.parent.right = delete_item.left
            delete_item.left.parent = delete_item.parent
            prev_most_right = delete_item.left.most_right()
            prev_most_right.right = delete_item.right
            if prev_most_right.right is not None:
                prev_most_right.right.parent = prev_most_right
            return None
        if delete_item.right is not None:
            delete_item.parent.right = delete_item.right
            delete_item.right.parent = delete_item.parent
            return None
        delete_item.parent.right = None
        # delete_item.clean()
        return None

    def to_list(self) -> List[T]:
        lst = []
        if self.left is not None:
            lst = self.left.to_list()
        lst.append(self.value)

        if self.right is not None:
            lst.extend(self.right.to_list())

        return lst

    def merge(self, other: Node[T]) -> None:
        for el in other.to_list():
            self.add(el)
        return None

    def deepness(self, level=0):
        if self.parent is None:
            return level
        return self.parent.deepness(level + 1)

    def visualization(self, new_line: bool = False, step_back=0) -> None:
        if new_line:
            print('\n' + ' ' * ((self.max_char_length + 3)
                  * (self.deepness() - step_back)), end='')

        if self.left is not None:
            print(str(self.value) + ' ' + '-' * (self.max_char_length -
                  self.char_length + 1) + ' ', end='')
            self.left.visualization(False)

        else:
            print(self.value, end='')

        if self.right is not None:
            self.right.visualization(True, step_back + 1)

    # works correctly only for the root
    def __str__(self) -> str:
        self.visualization()
        return ''

    def __repr__(self) -> str:
        self.visualization()
        return ''


class Tree[T]:
    root: Node[T] | None

    def __init__(self, any_node: Node[T] | None = None) -> None:
        if any_node is not None:
            self.root = any_node.get_root()
            return None
        self.root = None
        return None

    def correct(self) -> bool:
        if self.root is not None:
            return self.root.correct()
        return True

    def search(self, value: T) -> Node[T] | None:
        if self.root is not None:
            return self.root.search(value)
        return None

    def get_root(self) -> Node[T] | None:
        return self.root

    def add(self, value: T) -> None:
        if self.root is not None:
            self.root.add(value)
            return None
        self.root = Node(value)
        return None

    def delete(self, value: T) -> None:
        if self.root is None:
            return None

        delete_item = self.root.search(value)
        if delete_item is None:
            return None

        if value == self.root.value and self.root.left is None and self.root.right is None:
            self.root = None
            return None

        self.root.delete(value)

        furth = False
        if delete_item == self.root:
            change = None
            if delete_item.left is not None:
                change = delete_item.left.get_root()
            elif delete_item.right is not None:
                change = delete_item.right.get_root()
            elif delete_item.parent is not None:
                change = delete_item.parent.get_root()
            furth = True

        delete_item.clean()

        if furth:
            self.root = change
        return None

    def to_list(self) -> List[T]:
        if self.root is not None:
            return self.root.to_list()
        return []

    def merge(self, other: Node[T]) -> None:
        if self.root is not None:
            self.root.merge(other)
            return None
        self.root = other.get_root()

    def visualization(self, new_line: bool = False, step_back=0) -> None:
        if self.root is not None:
            self.root.visualization()
        return None

    def __str__(self) -> str:
        self.visualization()
        return ''

    def __repr__(self) -> str:
        self.visualization()
        return ''
