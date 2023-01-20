print("Hello World")

if 5 > 2:
    print("Five is greater than two!")

# This is a comment

"""
This is a comment
written in
more that just one line
"""

carname = "Volvo"

x = 50

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

myfirst_name = "John"

x = y = z = "Orange"


def myfunc():
    global x
    x = "fantastic"


x = 5
print(type(x))
# int


x = "Hello World"
print(type(x))
# str

x = 20.5
print(type(x))
# float

x = ["apple", "banana", "cherry"]
print(type(x))
# list

x = ("apple", "banana", "cherry")
print(type(x))
# tuple

x = {"name": "John", "age": 36}
print(type(x))
# dict

x = True
print(type(x))
# bool

x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print(10 > 9)
# True

print(10 == 9)
# False

print(10 < 9)
# False

print(bool("abc"))
# True

print(bool(0))
# False

print(10 * 5)

print(10 / 2)

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

if 5 != 10:
    print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

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

fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

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

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()

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

if a == b and c == d:
    print("Hello")

if a == b or c == d:
    print("Hello")

if 5 > 2:
    print("Five is greater than two!")

if 5 > 2: print("Five is greater than two!")

print("Yes") if 5 > 2 else print("No")

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


def my_function():
    print("Hello from a function")


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


x = lambda a: a


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


p2 = Person()


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

# import mymodule

# import mymodule as mx


#import mymodule
#print(dir(mymodule))


#from mymodule import person1