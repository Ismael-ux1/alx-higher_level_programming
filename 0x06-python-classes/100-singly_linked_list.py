#!/usr/bin/python3
# Class Node that defines a node of a singly linked list


class Node:
    """A node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list"""
    def __init__(self):
        # Initialize an empty linked list with no head nod
        self.head = None

    def sorted_insert(self, value):
        # Create a new node with the given value
        new_node = Node(value)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return

        if value < self.head.data:
            # If the value is > than the head, insert new node at the beginning
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None and value > current.next_node.data:
            # Traverse the list to find the correct position,
            # to insert the new node
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
