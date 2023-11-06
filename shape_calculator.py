class Rectangle:
    """An object that describe a rectangle polygon."""
    height: int
    width: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __repr__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """
        Compute the length of the diagonal.
        :return: √(width² + height²)
        """
        return (self.width ** 2 + self.height ** 2) ** .5  # √(width² + height²)

    def get_picture(self):
        """
        Returns a string that represents the shape using lines of "*".
        """
        pass

    def get_amount_inside(self, shape: 'Rectangle'):
        """
        Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        """
        if shape.width > self.width or shape.height > self.height:
            return False
        else:
            pass


class Square(Rectangle):
    """The Square class is a subclass of Rectangle."""

    def __init__(self, side_length: int):
        super().__init__(side_length, side_length)

    def __repr__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side_length):
        self.height = side_length
        self.width = side_length

    def set_width(self, width: int):
        self.set_side(width)

    def set_height(self, height: int):
        self.set_side(height)
