from __future__ import annotations
from typing import Callable
from enum import Enum, auto


class Compare(Enum):
    Less = auto()
    Equal = auto()
    Greater = auto()


class Node[T]:
    value: T
    left: Node[T] | None
    right: Node[T] | None
    parent: Node[T] | None
    predicate: Callable[[T, T], Compare]
    max_char_length: int

    def __init__(self, value: T, predicate: Callable[[T, T], Compare] | None = None) -> None:
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
            if not self.predicate(self.value, self.right.value) == Compare.Greater:
                return False
        return True

    def search(self, search_item: Node[T]) -> Node[T] | None:
        if self.predicate(self.value, search_item.value) == Compare.Equal:
            return self
        if self.predicate(search_item.value, self.value) == Compare.Less:
            if self.left is not None:
                return self.left.search(search_item)
        if self.predicate(search_item.value, self.value) == Compare.Greater:
            if self.right is not None:
                return self.right.search(search_item)
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

    def add(self, add_item: Node[T]) -> None:
        if self.predicate(add_item.value, self.value) == Compare.Less:
            if self.left is not None:
                self.left.add(add_item)
            else:
                self.left = add_item
                self.left.parent = self
                self.left.predicate = self.predicate

                if self.left.max_char_length > self.max_char_length:
                    self.get_root().change_max_char_length(self.left.max_char_length)
                else:
                    self.left.max_char_length = self.max_char_length

        if self.predicate(add_item.value, self.value) == Compare.Greater:
            if self.right is not None:
                self.right.add(add_item)
            else:
                self.right = add_item
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
        if self.parent is not None
            return self.predicate(self.value, self.parent.value) == Compare.Greater
        return None

    def is_left(self) -> bool | None:
        is_right_return = self.is_right()
        if is_right_return is not None:
            return not is_right_return
        return None

    def delete(self, delete_item: Node[T]) -> None:
        if self.search(delete_item) is None:
            return None
        right_part, left_part, parent_part = delete_item.right, delete_item.left, delete_item.parent
        if delete_item.is_left():
            parent_part.left = left_part
            if left_part is not None:
                right_part.parent = parent_part.left.most_right()
                parent_part.left.most_right().right = right_part
                left_part.parent = parent_part
            else:
                right_part.parent = parent_part
                parent_part.left = right_part
        else:
            parent_part.right = left_part
            if left_part is not None:
                right_part.parent = parent_part.most_right()
                parent_part.most_right().right = right_part
                left_part.parent = parent_part
            else:
                right_part.parent = parent_part
                parent_part.right = right_part

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

    def x(self) -> None:
        pass

def func(x: int, y: int) -> Compare:
    if x < y:
        return Compare.Less
    if x == y:
        return Compare.Equal
    return Compare.Greater


# a = Node(20, func)
# b = Node(30)
# c = Node(15)
# d = Node(19)
# e = Node(13)
# f = Node(14)
# g = Node(12)
# h = Node(10)
# i = Node(13.5)
# j = Node(12.5)
# k = Node(14.5)
# l = Node(12.7)
# m = Node(12.3)
# x = Node(31)
# y = Node(32)
# z = Node(33)
# p = Node(1)

# a.add(b)
# a.add(c)
# a.add(d)
# a.add(e)
# a.add(f)
# a.add(g)
# a.add(h)
# a.add(i)
# a.add(j)
# a.add(k)
# a.add(l)
# a.add(m)
# a.add(x)
# a.add(y)
# a.add(z)

a = Node(10, func)
b = Node(20)
c = Node(15)
d = Node(14)
e = Node(16)
f = Node(25)
g = Node(24)
h = Node(26)

a.add(b)
a.add(c)
a.add(d)
a.add(e)
a.add(f)
a.add(g)
a.add(h)

print(a)
a.delete(d)
print(a)
