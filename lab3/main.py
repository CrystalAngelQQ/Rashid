# Create a python file and import some of the functions from the above 13 tasks and try to use them.

from functions import *
from random import randint
print(solve(35, 94))

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

print(volume(10))

print(unique_list([1, 2, 3, 2, 1]))

print(is_palindrome('abcba'))
print(is_palindrome('abcbad'))

histogram([4, 9, 7])

game(randint(1, 20))