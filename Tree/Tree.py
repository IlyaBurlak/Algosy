from typing import Optional


class Node:
    def __init__(self, value: int, left: 'Node' = None, right: 'Node' = None):
        self._value = value
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node: 'Node'):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node: 'Node'):
        self._right = node

    @property
    def value(self):
        return self._value

    def print_tree(self, value=''):
        if self.left:
            self.left.print_tree(value + "-")
        print(f"{value} [{self.value}]")
        if self.right:
            self.right.print_tree(value + "-")


class BinaryTree:
    def __init__(self):
        self._head: Optional[Node] = None

    def insert(self, value: int):
        if self._head is None:
            self._head = Node(value)
        else:
            self._insert_node(self._head, value)

    def _insert_node(self, current_node: Node, value: int):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_node(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_node(current_node.right, value)

    def exists(self, value: int):
        if self._head is None:
            return False
        else:
            return self._exists(self._head, value)

    def _exists(self, current_node: Node, value: int):
        if current_node.value == value:
            return True
        elif current_node.value > value:
            if current_node.left:
                return self._exists(current_node.left, value)
            return False
        elif current_node.value < value:
            if current_node.right:
                return self._exists(current_node.right, value)
            return False

    def delete(self, value: int):
        if self._head is not None:
            if self._head.value == value:
                self._head = None
            else:
                self._delete(self._head, value)

    def _delete(self, current_node: Node, value: int):
        if current_node is not None:
            if current_node.left and current_node.left.value == value:
                current_node.left = None
            elif current_node.right and current_node.right.value == value:
                current_node.right = None
            else:
                if value < current_node.value:
                    if current_node.left:
                        return self._delete(current_node.left, value)
                elif value > current_node.value:
                    if current_node.right:
                        return self._exists(current_node.right, value)

    def next(self, value: int):
        all_value = []
        if self._head is not None and self._head.value != value:
            self._take_all(self._head, all_value)
        all_value.sort()
        for val in all_value:
            if val > value:
                return val

    def _take_all(self, current_node: Node, all_value: list):
        all_value.append(current_node.value)
        if current_node.left is not None:
            self._take_all(current_node.left, all_value)
        if current_node.right is not None:
            self._take_all(current_node.right, all_value)

    def prev(self, value: int):
        all_value = []
        if self._head is not None and self._head.value != value:
            self._take_all(self._head, all_value)
        all_value.sort(reverse=True)
        for val in all_value:
            if val < value:
                return val

    def show(self):
        if self._head is not None:
            self._head.print_tree()


            