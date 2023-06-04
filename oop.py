print('task1')
from math import pi

class Rectangle:

    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return 2 * (self.sideA + self.sideB)

class Circle(object):

    def __init__(self, r,):
        self.radius = r

    def getArea(self):
        return round(pi*(self.radius)**2)

    def getPerimeter(self):
        return round(2*pi*self.radius)

circy = Circle(52)
print(circy.getArea())
circy = Circle(5.24)
print(circy.getPerimeter())

print('task2')
class Calculator:

    def add(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 + self.n2

    def subtract(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 - self.n2

    def multiply(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 * self.n2

    def divide(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 / self.n2


calculator = Calculator()
print(calculator.add(12, 5))
print(calculator.subtract(15, 5))

print('task3')
class Person:

    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food_name):
        if food_name in self.likes:
            return f'{self.name} eats the {food_name} and loves it!'
        elif food_name in self.hates:
            return f'{self.name} eats the {food_name} and hates it!'
        else:
            return f'{self.name} eats the {food_name}!'


p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))

print('task4')
class OnesThreesNines:
    def __init__(self, num):
        self.__num = num

    @property
    def ones(self):
        return self.__num

    @property
    def threes(self):
        return self.__num//3

    @property
    def nines(self):
        return self.__num//9


print('task5')
class Player:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"






