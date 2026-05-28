class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        # Area = width * height
        return self.width * self.height

    def get_perimeter(self):
        # Perimeter = 2 * width + 2 * height
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        # Diagonal = (width^2 + height^2)^0.5
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Validate that the shape is not too large for a text picture
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        # Build the picture line by line using string repetition
        line = "*" * self.width + "\n"
        return line * self.height

    def get_amount_inside(self, other_shape):
        # Use floor division to find how many times the other shape fits horizontally and vertically
        horizontal_fit = self.width // other_shape.width
        vertical_fit = self.height // other_shape.height
        return horizontal_fit * vertical_fit

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Initialize both width and height to the given side length using the parent class
        super().__init__(side, side)

    def set_side(self, side):
        # Set both tracking dimensions to ensure consistency
        self.width = side
        self.height = side

    def set_width(self, width):
        # Overrides parent to ensure squares stay proportional
        self.set_side(width)

    def set_height(self, height):
        # Overrides parent to ensure squares stay proportional
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Rectangle Area:", rect.get_area())
    rect.set_height(3)
    print("Rectangle Perimeter:", rect.get_perimeter())
    print("Rectangle String:", rect)
    print("Rectangle Picture:\n" + rect.get_picture())

    sq = Square(9)
    print("Square Area:", sq.get_area())
    sq.set_side(4)
    print("Square Diagonal:", sq.get_diagonal())
    print("Square String:", sq)
    print("Square Picture:\n" + sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print("Amount of Squares Inside Rectangle:", rect.get_amount_inside(sq))
