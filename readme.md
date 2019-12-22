# Python Special Methods
This repository is part of my studies about Python's special methods and data model, here, I intent to cover many topics of theses subjects with pratic samples and a few words.

# repr()
Most used on debbuging, the builtin method `repr()` return an official string that represents the object, in best practices, this string should represent how to recreat that object. 

> code example: 

```python

class MyClass:
    
    def __init__(self, param_1, param_n):
        self.p_1 = param_1
        self.p_n = param_n

    def __repr__(self):
        return "MyClass(param_1, param_n)"

```