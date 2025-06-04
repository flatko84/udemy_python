from functools import total_ordering
import math

@total_ordering
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Vector(x: '{self.x}', y: '{self.y}', z: '{self.z}')"
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The object must be of the class Vector.")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        if type(other) not in [int, float]:
            raise TypeError("Vectors can only be multiplied by integers or floats.")
        return Vector(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other): # check if needed
        if type(other) not in [int, float]:
            raise TypeError("Vectors can only be multiplied by integers or floats.")
        return self * other
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The object must be of the class Vector.")
        return abs(self) == abs(other)
    
    def __gt__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The object must be of the class Vector.")
        return abs(self) > abs(other)
    
    def __abs__(self):
        return math.sqrt(sum([getattr(self, coordinate) ** 2 for coordinate in ['x', 'y', 'z']]))
    
    def __hash__(self):
        return hash(abs(self))
    
    def __bool__(self):
        return bool(abs(self)) 
    
    def __getitem__(self, item):
        if type(item) is not str:
            raise TypeError("The key must be of a type string.")
        item = item.lower()
        if item not in ['x', 'y', 'z']:
            raise ValueError("The key must be either x, y or z.")
        return getattr(self, item)
    

v1 = Vector(2, 4, 6)
print(v1)
print(abs(v1)) # 7.48331477
v2 = Vector(1,1,1)
print(abs(v2)) # srt of 3
print(v1 + v2) #8.48331477
print(v1*2.5)
print(2.5*v1)
print(v1 <= v2)
print(v2 < v1)
print(bool(v1))
v3 = Vector(0, 0, 0)
print(bool(v3))
print(v1['y'])
