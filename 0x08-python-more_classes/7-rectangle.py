#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    class that defines Rectangle
    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    Raises:
        TypeError: when width/height not int type
        ValueError: when width/height less than 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init method to construct a rectangle
        """
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        width getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter attribute
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height setter attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        the rectangle area
        Returns:
            the current rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        the rectangle perimetre
        Returns:
            the current rectangle perimetre
        """
        if (self.__height == 0) or (self.__width == 0):
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        print a rectangle
        """
        _str = ""
        if (self.__height == 0) or (self.__width == 0):
            return ("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    _str += str(self.print_symbol)
                if i < self.__height - 1:
                    _str += "\n"
            return (_str)

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1
