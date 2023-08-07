#!/usr/bin/python3

""" Class Node that defines a node of a singly linked list """


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" class that defines a singly lined list """

class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with no head node
        self.head = None

    def sorted_insert(self, value):
        # Create a new node with the given value
        new_node = Node(value)

        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return

        if value < self.head.data:
            # If the value is < the head, insert new node at the beginning
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and value > current.next_node.data:
            # Traverse the list to find the correct position to insert
            # the new node
            current = current.next_node

        # Insert the new node in sorted order
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        # Convert the linked list to a string for printing
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next_node
        return '\n'.join(map(str, result))

    # Example usage:


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.sorted_insert(5)
    linked_list.sorted_insert(2)
    linked_list.sorted_insert(8)
    linked_list.sorted_insert(3)
    print(linked_list)
