# Python Special Methods
This repository is part of my studies about Python's special methods and data model, here, I intent to cover many topics of theses subjects with pratic samples and a few words.

# repr()
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

# str()
As `repr()` built-in function, `str()` return a `string`, but an informal representation without the commitment of be an valid python expression.

```python
class MyClass:
    
    def __init__(self, param_1, param_n):
        self.p_1 = param_1
        self.p_n = param_n

    def __str__(self):
        return f"MyClass has attributes param_1 with value {self.p_1} and param_n equals to {self.p_n})"

```