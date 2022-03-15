from __future__ import annotations
from dataclasses import dataclass
from typing import Union


@dataclass
class Node:
    next: Union[Node, None] = None
    prev: Union[Node, None] = None
    value: int = 0


@dataclass
class LinkedList:
    current_node: Union[Node, None] = None
    head: Union[Node, None] = None
    tail: Union[Node, None] = None
    size: int = 0

    def push(self):
        """
        Add a node to the linked list.
        At the end, current node is at the end of the list.
        """
        node = Node()
        if self.tail == None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.current_node = node
        self.size += 1

    def left(self):
        """
        Move to the left in the linked list.
        Do nothing if current node is None or at the start of the list.
        """
        if self.current_node == self.head or self.current_node == None:
            return
        self.current_node = self.current_node.prev

    def right(self):
        """
        Move to the right in the linked list.
        Add a Node to the list if current Node
        if None or at the end of the list.
        """
        if self.current_node == None or self.current_node == self.tail:
            self.push()
        else:
            self.current_node = self.current_node.next

    def current_node_inc(self):
        """
        Increment current node value.
        If current node is None, push a Node and increment it.
        """
        if self.current_node == None:
            self.push()
            self.current_node_inc()
        else:
            self.current_node.value += 1

    def current_node_dec(self):
        """
        Decrement current node value if current value is > 0.
        If current node is None, push a Node and decrement it.
        """
        if self.current_node == None:
            self.push()
            self.current_node_dec()
        elif self.current_node.value > 0:
            self.current_node.value -= 1

    def current_node_get_value(self) -> int:
        """
        Return the current value of the Node.
        If node is None return 0.
        """
        if self.current_node == None:
            return 0
        return self.current_node.value

    def current_node_set_value(self, value: int):
        """
        Set the current node value to value parameter.
        If current node is None do nothing.
        """
        if self.current_node == None:
            return
        self.current_node.value = value

    def __str__(self) -> str:
        """
        Return a string representation of the current linked list.
        """
        s = ""
        curr = self.head
        while curr != None:
            s += "| "
            s += str(curr.value)
            s += " |"
            curr = curr.next
            if curr != None:
                s += " -> "
        return s
