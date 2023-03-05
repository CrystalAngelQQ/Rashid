# Python builtin functions exercises
import math
import time


# Write a Python program with builtin function to multiply all the numbers in a list
def multiply_in_list(numbers: list) -> float:
    product: float = 1
    for x in numbers:
        product *= x
    return product


input_str = input("Enter the numbers in the list separated by spaces: ")
floats = [float(number) for number in input_str.split()]
result = multiply_in_list(floats)
print(f"The product of the numbers in the list is: {result}")


# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters
# and lower case letters
def upper_and_lower_count(string: str) -> (int, int):
    upper_letters: list = list(filter(lambda x: x.isupper(), string))
    lower_letters: list = [x for x in string if x.islower()]

    return len(upper_letters), len(lower_letters)


input_str = input("Enter a string: ")
upper_count, lower_count = upper_and_lower_count(input_str)
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")


# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(string: str) -> bool:
    reversed_text = "".join(reversed(string))
    return reversed_text == string


input_str = input("Enter a string: ")
result = is_palindrome(input_str)
if result:
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")


# Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858
def delayed_sqrt(number: float, delay_ms: int) -> float:
    time.sleep(delay_ms / 1000)
    sqrt_num = math.sqrt(number)
    return sqrt_num


num = float(input("Enter a number to find its square root: "))
delay = int(input("Enter the delay time in miliseconds: "))
result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} miliseconds is {result}")


# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t: tuple) -> bool:
    return all(t)


input_str = input("Enter a list of boolean values separated by spaces: ")
bool_tuple = tuple([bool(x) for x in input_str.split()])
result = all_true(bool_tuple)
if result:
    print("All elements of the tuple are True.")
else:
    print("Not al elements of the tuple are True.")
