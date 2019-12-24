class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"


if (__name__ == "__main__"):
    print("# repr()")
    point = Point(x=20, y=9)
    print(f"\t{repr(point)}")
