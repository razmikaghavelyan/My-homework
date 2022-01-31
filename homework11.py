class Triangle:
    triagnle_instance = 0
    def __init__(self, side_1, side_2, side_3):
        Triangle.triagnle_instance += 1
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def triangle_area(self):
        return (self.side_1 + self.side_2 + self.side_3) / 2

    def perimeter_triangle(self):
        return self.side_1 + self.side_2 + self.side_3

    def __eq__(self, other):
        return self.triangle_area() == other.triangle_area() and self.perimeter_triangle() == other.perimeter_triangle()

    def __lt__(self, other):
        return self.triangle_area() < other.triangle_area() and self.perimeter_triangle() < other.perimeter_triangle

triangle_1 = Triangle(4, 5, 6)
triangle_2 = Triangle(6, 5, 4)

print(triangle_1 == triangle_2)
print(triangle_1 < triangle_2)



class Rectangular:
    instance_counter = 0

    def __init__(self, height, length):
        Rectangular.instance_counter += 1
        self.height = height
        self.length = length

    def rectangular_area(self):
        return self.height * self.length

    def __eq__(self, other):
        return self.height == other.height and self.length == other.length

    def __gt__(self, other):
        return self.rectangular_area() > other.rectangular_area()


rectangular_1 = Rectangular(8, 6)
rectangular_2 = Rectangular(6, 8)
