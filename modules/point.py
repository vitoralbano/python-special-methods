class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"Point located at X {self.x} and Y {self.y}"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)



if (__name__ == "__main__"):
    print("# __repr__()")
    point = Point(x=20, y=9)
    print(f"{repr(point)}")

    print("\n# __str__()")
    print(point)

    print("\n# __add__()")
    point_2 = Point(x=6, 12)
    print(f"{repr(point)} + {repr(point_2)}")
    print(f"{repr(point + point_2)}")
