class Point:
    default_color = "red"
    # this is a class attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
        # by default __str__ returns name of class and memory address, here we're overriding

        # this is basically like toString() in Java i guess, so without even calling this method, it'll be called when you pass this to print!

        # you can also convert point object to string using this method like > str(point)

    @classmethod
    def zero(cls):
        return cls(0, 0)
        # this is a class method

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        # if you don't have the __str__ magic method, don't print addition of 2 points right away, rather do this >
        # combined = point + other, in the next line >
        # print(combined.x)


point = Point(1, 2)
other = Point(0, 1)
type(point)
isinstance(point, Point)
print(point > other)

combined = point + other
