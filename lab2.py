fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

## Python Tuples
fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

## Python Sets
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

## Python Dictionaries
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.get("model"))

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car["year"] = 2020

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car["color"] = "red"

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()

## Python If... Else
a = 50
b = 10
if a > b:
    print("Hello World")

a = 50
b = 10
if a != b:
    print("Hello World")

a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

c = d = 1  # Not in exercise
if a == b and c == d:
    print("Hello")

if a == b or c == d:
    print("Hello")

if 5 > 2:
    print("Five is greater than two!")

if 5 > 2:
    print("Five is greater than two!")

print("Yes") if 5 > 2 else print("No")

## Python While Loops
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

## Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


## Python Functions
def my_function():
    print("Hello from a function")


my_function()


def my_function(fname, lname):
    print(fname)


def my_function(x):
    return x + 5


def my_function(*kids):
    print("The youngest child is " + kids[2])


def my_function(**kid):
    print("His last name is " + kid["lname"])


## Python Lamnda
x = lambda a: a


## Python Classes
class MyClass:
    x = 5


class MyClass:
    x = 5


p1 = MyClass()


class MyClass:
    x = 5


p1 = MyClass()

print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


## Python Inheritance
class Student(Person):
    pass  # not in exercise


class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()
