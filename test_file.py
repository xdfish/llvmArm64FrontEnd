from enum import Enum

class test(Enum):
    a = "abc"
    b = "def"


print("abc" in test.name)