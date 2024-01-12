class Shoe:

    def __init__(self, brand, size=0):
        self.brand = brand
        self._size = size  # instance attribute

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else: 
            print("Size must be an integer")

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    @property
    def material(self):
        return self._material
    
    @material.setter
    def material(self, material):
        self._material = material
    
# Example usage
le_bron = Shoe("Nike")
le_bron.size = 14
print(le_bron.size)
le_bron.size = "14"  # This will print an error message
print(le_bron.size)
le_bron.color = "Dark Green"
print(le_bron.color)
le_bron.material = "Leather"
print(le_bron.material)