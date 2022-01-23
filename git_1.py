import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return round(math.pi * (self.radius**2), 3)

    def circle_perimeter(self):
        return round(2 * math.pi * self.radius, 3)


circle_math = Circle(5)

print(circle_math.circle_area(), circle_math.circle_perimeter(), sep="\n")


class Human:
    def __init__(self, name, surname, age, height, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight

    def human_age(self):
        return f"{2022 - self.age + 100} In this year you must be 100"

    def human_weight(self):
        if self.age < 40:
            if self.height - 110 < self.weight:
                return f"{self.height - 110} That's your optimal weight.You must gain weight {self.weight - (self.height -110)} kg"
            elif self.height - 110 > self.weight:
                return f"{self.height - 110} That's your optimal weight.You must lose weigh {(self.height - 110) - self.weight} kg"
            else:
                return "You already have optimal weight. Congratulations!"
        elif self.age > 40:
            return f"{self.height - 100}That's your optimal weight. But I recomended you chill and have fun"

    def me_myself(self):
        return f"Hi my name is {self.name} {self.surname} i'm {self.age} years old"


my_attributes = Human("Razmik", "Aghavelyan", 23, 176, 80)
print(my_attributes.human_age(), my_attributes.human_weight(), my_attributes.me_myself(), sep="\n")