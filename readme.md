# Python Special Methods
This repository is part of my studies about Python's special methods and data model, here, I intent to cover many topics of theses subjects with pratic samples and a few words.

# Simple customizations

## `__repr__`
Most used on debugging, the built-in method `repr()` return an official string that represents the object, in best practices, this string should represent how to recreate that object. 

> code example: 

```python

class MyClass:
    
    def __init__(self, param_1, param_n):
        self.p_1 = param_1
        self.p_n = param_n

    def __repr__(self):
        return f"MyClass(param_1={self.p_1}, param_n={self.p_n})"

```

## `__str__`
As `repr()` built-in function, `str()` return a `string`, but an informal representation without the commitment of be an valid python expression.

```python
class MyClass:
    
    def __init__(self, param_1, param_n):
        self.p_1 = param_1
        self.p_n = param_n

    def __str__(self):
        return f"MyClass has attributes param_1 with value {self.p_1} and param_n equals to {self.p_n})"

```

# Emulating numeric types
## `__add__`
Used for arithmetic operations, the method `__add__` allows to sum two instances of the same class or classes that inherit common attributes.

As the commited code, lets see it with simple example:
```python
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

```python
>>> point_1 = Point(2, 4)
>>> point_2 = Point(3, 5)
>>> point_1 + point_2
Point(x=5, y=9)
```
