#!/usr/bin/python3
"""Define Node and SinglyLinkedList classes"""


class Node:
    """Representation of a node of a singly linked list

    Attributes:
    data (int): value of entry in the node
    next_node (Node): The next instance of Node or None
    """
    def __init__(self, data, next_node=None):
        """Initialize a new instance of a node

        Args:
        data (int): value of entry in the node
        next_node (Node): The next instance of Node or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data attribute of Node

        Returns:
            The value of data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Assign value to data attribute

        Args:
        value (int): The value of data or raise error
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get next_node attribute of node

        Returns:
        The value of the next node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set value to next_node attribute
        Args:
        value (Node): The next node or raise an error
        """
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a node object')
        self.__next_node = value


class SinglyLinkedList:
    """Representation of a singly linked list"""

    def __init__(self):
        """Initialize an instance of SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert node to SinglyLinkedList in an ordered (increasing) manner

        Args:
        value (int): data value of the node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define __str__ method for print of SinglyLinkedList

        Returns:
            printable string representation
        """
        val_list = []
        tmp = self.__head
        while tmp is not None:
            val_list.append(str(tmp.data))
            tmp = tmp.next_node
        return('\n'.join(val_list))
