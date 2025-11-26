from typing import Self


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_x_int(self): return int(self.x)
    def get_y_int(self): return int(self.y)
    def get_z_int(self): return int(self.z)
    def __str__(self) -> str: return f"{self.x}, {self.y}, {self.z}"
    
    
    def __mul__(self, other:int | float | Self) -> Self:
        object_vector_mul = Vector(self.x * other, self.y * other, self.z * other)

        return object_vector_mul
    
    def __rmul__(self, other:int | float | Self) -> Self: return self * other
    
    
    def __add__(self, other:int | float | Self) -> Self:
        if type(other) == int or type(other) == float: object_vector_add = Vector(self.x + other, self.y + other, self.z + other)
        elif type(other) == Vector: object_vector_add = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else: raise TypeError(f"A vector cannot be combined with {type(other)}")
        
        return object_vector_add

    def __radd__(self, other:int | float | Self) -> Self: return self + other
    
    
    def __sub__(self, other:int | float | Self) -> Self:
        if type(other) == int or type(other) == float: object_vector_sub = Vector(self.x - other, self.y - other, self.z - other)
        elif type(other) == Vector: object_vector_sub = Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else: raise TypeError(f"Subtraction error")
        
        return object_vector_sub
    
    def __rsub__(self, other:int | float | Self) -> Self: return self - other
    
    
    def __truediv__(self, other:int | float | Self) -> Self:
        object_vector_div = Vector(self.x / other, self.y / other, self.z / other)

        return object_vector_div
    
    def __rtruediv__(self, other:int | float | Self) -> Self: return self / other
    
    
    def module(self) -> float:
        lenght = (self.x**2 + self.y**2 + self.z**2)**0.5

        return lenght
        
        
    def normalized(self) -> Self:
        lenght = self.module()
        norm = Vector(self.x/lenght, self.y/lenght, self.z/lenght)
        
        return norm