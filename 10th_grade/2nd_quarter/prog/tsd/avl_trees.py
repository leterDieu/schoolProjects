from __future__ import annotations

from enum import nonmember
from types import MethodType
from typing import Callable, Tuple

from trees import Node, Compare


class AVLNode[T](Node[T]):
    height: int
    left: AVLNode[T] | None
    right: AVLNode[T] | None
    parent: AVLNode[T] | None

    def __init__(
        self,
        value: T,
        predicate: Callable[[T, T], Compare] = lambda first, second: (
            Compare.Less
            if first < second
            else (Compare.Greater if first > second else Compare.Equal)
        ),
    ) -> None:
        super().__init__(value, predicate)
        self.height = 0

    def get_root(self) -> AVLNode[T]:
        if self.parent is None:
            return self
        return self.parent.get_root()

    def get_height(self) -> int:
        left_height, right_height = 0, 0
        if self.left is not None:
            left_height = self.left.get_height() + 1
        if self.right is not None:
            right_height = self.right.get_height() + 1
        return max(left_height, right_height)

    def set_right_height_to_one(self) -> None:
        self.height = self.get_height()

    def set_right_height_cascade(self) -> None:
        self.set_right_height_to_one()
        if self.left is not None:
            self.left.set_right_height_cascade()
        if self.right is not None:
            self.right.set_right_height_cascade()
        return None

    def set_right_height_all(self) -> None:
        self.get_root().set_right_height_cascade()

    def are_child_heights_acceptable(self) -> bool:
        if self.left is not None and self.right is not None:
            if abs(self.left.height - self.right.height) > 1:
                return False
            return True
        if self.left is None and self.right is None:
            return True
        if self.right is not None:
            if self.right.height > 0:
                return False
        if self.left is not None:
            if self.left.height > 0:
                return False
        return True

    def are_heights_acceptable_cascade(self) -> bool:
        if not self.are_child_heights_acceptable():
            return False
        if self.left is not None:
            if not self.left.are_heights_acceptable_cascade():
                return False
        if self.right is not None:
            if not self.right.are_heights_acceptable_cascade():
                return False
        return True

    def correct(self) -> bool:
        return super(AVLNode, self).correct() and self.are_heights_acceptable_cascade()

    def left_rotation(self) -> None:
        if self.right is None:
            return None
        # if self.right.right is None:
        #     return None

        self.right.parent = self.parent

        if self.parent is not None:
            if self.is_left():
                self.parent.left = self.right
            else:
                self.parent.right = self.right

        self.parent = self.right
        self.right = self.right.left
        if self.right is not None:
            self.right.parent = self
        self.parent.left = self

        return None

    def right_rotation(self) -> None:
        if self.left is None:
            return None
        # if self.left.left is None:
        #     return None

        self.left.parent = self.parent

        if self.parent is not None:
            if self.is_left():
                self.parent.left = self.left
            else:
                self.parent.right = self.left

        self.parent = self.left
        self.left = self.left.right
        if self.left is not None:
            self.left.parent = self
        self.parent.right = self

        return None

    def left_right_rotation(self) -> None:
        if self.left is None:
            return None
        if self.left.right is None:
            return None

        self.left.left_rotation()
        self.right_rotation()
        return None

    def right_left_rotation(self) -> None:
        if self.right is None:
            return None
        if self.right.left is None:
            return None

        self.right.right_rotation()
        self.left_rotation()
        return None

    def balance(self) -> None:
        if self.left is None and self.right is None:
            return None
        if self.left is not None and self.right is not None:
            if self.left.height - self.right.height > 1:
                if self.left.left is None:
                    self.left_right_rotation()
                    return None
                if self.left.right is None:
                    self.right_rotation()
                    return None
                if self.left.right.height > self.left.left.height:
                    self.left_right_rotation()
                    return None
                self.right_rotation()
                return None
            if self.right.height - self.left.height > 1:
                if self.right.right is None:
                    self.right_left_rotation()
                    return None
                if self.right.left is None:
                    self.left_rotation()
                    return None
                if self.right.left.height > self.right.right.height:
                    self.right_left_rotation()
                    return None
                self.left_rotation()
                return None
            return None
        if self.left is not None:
            if self.left.height > 0:
                if self.left.left is None:
                    self.left_right_rotation()
                    return None
                if self.left.right is None:
                    self.right_rotation()
                    return None
                if self.left.right.height > self.left.left.height:
                    self.left_right_rotation()
                    return None
                self.right_rotation()
                return None
            return None
        if self.right.height > 0:
            if self.right.right is None:
                self.right_left_rotation()
                return None
            if self.right.left is None:
                self.left_rotation()
                return None
            if self.right.left.height > self.right.right.height:
                self.right_left_rotation()
                return None
            self.left_rotation()
            return None
        return None

    def balance_cascade(self) -> None:
        if self.left is not None:
            if not self.left.correct():
                self.left.balance_cascade()
                self.set_right_height_all()
        if self.right is not None:
            if not self.right.correct():
                self.right.balance_cascade()
                self.set_right_height_all()
        if not self.correct():
            self.balance()
            self.set_right_height_all()
        return None

    def add_without_balance(self, value: T) -> None:
        # note: it's the same code as in Node, except it uses AVLNode, not Node to create a new [AVL]Node,
        # that's why it wasn't possible to write super(AVLNode, self).add(value)
        if self.predicate(value, self.value) == Compare.Less:
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = AVLNode(value)
                self.left.parent = self
                self.left.predicate = self.predicate

                if self.left.max_char_length > self.max_char_length:
                    self.get_root().change_max_char_length(self.left.max_char_length)
                else:
                    self.left.max_char_length = self.max_char_length

                self.set_right_height_all()

        if self.predicate(value, self.value) == Compare.Greater:
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = AVLNode(value)
                self.right.parent = self
                self.right.predicate = self.predicate

                if self.right.max_char_length > self.max_char_length:
                    self.get_root().change_max_char_length(self.right.max_char_length)
                else:
                    self.right.max_char_length = self.max_char_length

                self.set_right_height_all()

        return None

    def add(self, value: T) -> None:
        self.add_without_balance(value)

        added_item = self.search(value)
        if added_item is None:
            return None

        self.get_root().balance_cascade()

        return None

    def search(self, value: T) -> AVLNode[T] | None:
        if self.predicate(self.value, value) == Compare.Equal:
            return self
        if self.predicate(value, self.value) == Compare.Less:
            if self.left is not None:
                return self.left.search(value)
        if self.predicate(value, self.value) == Compare.Greater:
            if self.right is not None:
                return self.right.search(value)
        return None

    def most_right(self) -> AVLNode[T]:
        if self.right is not None:
            return self.right.most_right()
        return self

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

        self.set_right_height_all()
        self.balance_cascade()
        return None

    def to_list(self) -> list[T]:
        return super(AVLNode, self).to_list()

    def merge(self, other: AVLNode[T]) -> None:
        for el in other.get_root().to_list():
            self.add(el)
        return None


class AVLTree[T]:
    root: AVLNode[T] | None

    def __init__(self, any_node: AVLNode[T] | None = None) -> None
        if any_node is not None:
            self.root = any_node.get_root()
            return None
        self.root = None
        return None

    def correct(self) -> bool:
        if self.root is not None:
            return self.root.correct()
        return True

    def search(self, value: T) -> AVLNode[T] | None:
        if self.root is not None:
            return self.root.search(value)
        return None

    def get_root(self) -> AVLNode[T] | None:
        return self.root

    def add(self, value: T) -> None:
        if self.root is not None:
            self.root.add(value)
            self.root = self.root.get_root()
            return None
        self.root = AVLNode(value)
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
        self.root = self.root.get_root()

        return None
