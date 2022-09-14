class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Triangle: {self.a}, {self.b}, {self.c}"

triangle_1 = Triangle(3, 4, 5)
print(triangle_1)                           # Triangle: 3, 4, 5

