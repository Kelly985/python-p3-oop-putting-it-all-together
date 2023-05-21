#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size_count(self):
        return self.size

    @size_count.setter
    def size_count(self, value):
        if not isinstance(value, int):
            ValueError("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

adidas = Shoe("stansmith",22 )


print(adidas.size_count)  
