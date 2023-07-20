#!/usr/bin/python3
""" Rectangle class that inherits from Base. """

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.

    Attributes:
          width (int): Width of the rectangle.
          height (int): height of the rectangle.
          x (int): X coordinate of the rectangle's position.
          y (int) Y coordinate of the rectangle's position.
          id (int): ID of the rectangle.

    Methods:
          __init__(self, width, height, x=0, y=0, id=None):
          Initialiea new instance of the Rectangle class
          display(self): Print the Rectangle instance with
          '#' characters representing the rectangle's shape.
        __str__(self): Return a string representation of the,
        Rectangle incetance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance if the Rectangle class.

        Args:
          width (int): Width of the rectangle.
          height (int): Height of the rectangle.
          x (int): X coordinate of the rectangle's position (default: 0).
          y (int): Y coordinate of the rectangle's position (default: 0).
          id (int): ID of the rectangle.

        Raises:
          TypeError: If width, height, x, y, or y is not an integer
          ValueError: If width or height is less than or equal to 0
          or if or y is less than 0.

        Notes:
         - The Rectangle class inherits the ID management from the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attriibute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with '#' characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Update the class Rectangle"""
        rect1 = f"({self.id}) {self.__x}/{self.__y}"
        rect2 = f"{self.__width}/{self.__height}"
        return f"[Rectangle] {rect1} - {rect2}"

    def update(self, *args, **kwargs):
        """
        Assign arguments to attribute of the Rectangle
        instance using key/value pairs.

        Args:
          *args: Positional arguments.
          **kwargs: Key-Value arguments representing attributes to update.

        Notes:
           - If *args exists and is not empty, **kwargs isskipped.
           - Each key in **kwargs represents an attribute of the Rectangle
           - Argument order is not important when using **kwargs.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representaion of a Recatngle. """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
            }
