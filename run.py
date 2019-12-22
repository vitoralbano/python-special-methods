from modules.point import Point


def run():
    print("\nPython Special methods".upper())
    print(f"{32*'-'}\n")

    print("# repr() of Point Class:")
    point = Point(20, 9)
    print(f"\t{repr(point)}")

    print("\n\n")


if __name__ == "__main__":
    run()