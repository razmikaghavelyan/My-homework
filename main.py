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

    def is_alike(self, other):
        if self.triangle_area() == other.triangle_area() or self.perimeter_triangle() == other.perimeter_triangle():
            return True


triangle_1 = Triangle(4, 5, 6)
triangle_2 = Triangle(6, 5, 4)

# print(triangle_2.triangle_area())
# print(triangle_1)


class Rectangular:
    instance_counter = 0

    def __init__(self, height, length):
        Rectangular.instance_counter += 1
        self.height = height
        self.length = length

    def rectangular_area(self):
        return self.height * self.length

    def contains_rec(self, other):
        if rectangular_1.rectangular_area() > other.rectangular_area():
            return "It can contains on it"
        else:
            return "It cant contain"

    def __eq__(self, other):
        if self.height == other.height and self.length == other.length:
            return "Its equal rectangular"
        else:
            return "They don't equal"


rectangular_1 = Rectangular(8, 6)
rectangular_2 = Rectangular(6, 8)
# print(rectangular_1.instance_1)
print(rectangular_1.__eq__(rectangular_2))