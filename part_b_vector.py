# Part B - Custom Vector class with dunder methods

class Vector:
    def __init__(self, values):
        # store values as a tuple
        self.values = tuple(values)

    def __add__(self, other):
        # both vectors must have same length
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same length for addition")
        result = tuple(a + b for a, b in zip(self.values, other.values))
        return Vector(result)

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same length for subtraction")
        result = tuple(a - b for a, b in zip(self.values, other.values))
        return Vector(result)

    def __mul__(self, scalar):
        # scalar multiplication
        result = tuple(a * scalar for a in self.values)
        return Vector(result)

    def __repr__(self):
        return f"Vector{self.values}"


# --- Testing ---
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))

print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 3  =", v1 * 3)
print("v2 * 2  =", v2 * 2)

# another test
v3 = Vector((10, 20))
v4 = Vector((5, 15))
print("\nv3 =", v3)
print("v4 =", v4)
print("v3 + v4 =", v3 + v4)
print("v3 * 0  =", v3 * 0)
