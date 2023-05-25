#!/usr/bin/env python3

class Shoe:

    def __init__(self, brand, size=0):
        self.brand = brand
  
        self._size = size
        #instance attribute

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else: 
            print("not an integer")

    size = property(get_size, set_size)

    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = color
    
    color = property(get_color, set_color)
        
    def get_material(self):
        return self._material
    
    def set_material(self, material):
        self._material = material

    material = property(get_material, set_material)
    
le_bron = Shoe("Nike")
le_bron.size = 14
print(le_bron.size)
le_bron.size = "14"
print(le_bron.size)
le_bron.color = "Dark Green"
print(le_bron.color)
le_bron.material = "Leather"
print(le_bron.material)