class Triangle:
    triangle_instance = 0

    def __init__(self, side_1, side_2, side_3):
        list_1 = sorted((side_1, side_2, side_3))
        if list_1[0] < list_1[2] - list_1[1]:
            raise ValueError("There is no triangle like that")
        Triangle.triangle_instance += 1
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def triangle_area(self):
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        res = (p*(p - self.side_1) * (p - self.side_2) * (p - self.side_3)) ** 0.5
        return round(res, 3)

    def perimeter_triangle(self):
        return self.side_1 + self.side_2 + self.side_3

    def __eq__(self, other):
        return self.triangle_area() == other.triangle_area() and self.perimeter_triangle() == other.perimeter_triangle()

    def __lt__(self, other):
        return self.triangle_area() <= other.triangle_area() and self.perimeter_triangle() <= other.perimeter_triangle()


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


triangle_1 = Triangle(5, 5, 5)
triangle_2 = Triangle(3, 5, 7)
print(triangle_1.triangle_area(), triangle_2.triangle_area())

triangle_1.triangle_area()
print(triangle_1 == triangle_2)
print(triangle_1 < triangle_2)

rectangular_1 = Rectangular(8, 6)
rectangular_2 = Rectangular(6, 8)
