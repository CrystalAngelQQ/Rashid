import math


# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to
# print the string in upper case.
class Upper:
    # не
    def getString(self):
        return input()

    def printString(self, string):
        print(string.upper())


# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length
# as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by
# default.
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# 3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by
# a length and width. The Rectangle class has a method which can compute the area.
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        super().__init__(length)
        self.width = width

    def area(self) -> float:
        return self.length * self.width


# 4. Write the definition of a Point class. Objects from this class should have a
#
#         a method show to display the coordinates of the point
#         a method move to change these coordinates
#         a method dist that computes the distance between 2 points


class Point:
    def __init__(self, *dimensions):
        self.dimensions = dimensions

    def print_coordinates(self):
        result = ""
        for dimension in self.dimensions:
            end = str(dimension) + " "
            result += end
        print(result)

    def change_coordinates(self, dimensions):
        self.dimensions = dimensions

    def compute_distance(self, other):
        result = 0

        for dimension, other_dimension in zip(self.dimensions, other.dimensions):
            squar = (dimension - other_dimension) ** 2
            result += squar

        return math.sqrt(result)


p1 = Point(1, 2, 3)
p2 = Point(1, 1, 1)
print(p1.compute_distance(p2))


# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals
# may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to
# make sure the account can't be overdrawn.


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        new_balance = self.balance + money
        self.balance = new_balance

    def withdraw(self, money):
        new_balance = self.balance - money
        if new_balance < 0:
            print(f"Мало, {new_balance}")

        self.balance = new_balance


my_account = Account("Рашид", 0)
my_account.deposit(200)
my_account.withdraw(100)
my_account.withdraw(400)


# 6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define
# anonymous functions.
is_prime = lambda x: all(x % i != 0 for i in range(2, int(x / 2) + 1))
result = list(filter(is_prime, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 23]))
print(f"Prime numbers: {result}")
