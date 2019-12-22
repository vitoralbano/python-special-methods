class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"


if (__name__ == "__main__"):
    print("# repr()")
    point = Point(20, 9)
    print(f"\t{repr(point)}")
