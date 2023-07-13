#!/usr/bin/python3
""" A class that defines a square. """


class Square:
    """ A class that defines a square. """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor method for Square.

        Parameters:
        - size (int): Optional. The size of the square. Default is 0.
        - position (tuple): Optional. The position of the square

        Raises:
        - TypeError: If size is not an integer
        - ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
        - value (int): The size of the square.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Parameters:
        - value (tuple): The position of the square.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        - ValueError: If value contains negative values.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#'.

        If size is equal to 0, print an empty line.
        Use the position to adjust the starting point of the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
