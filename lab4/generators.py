# # Python iterators and generators
# 1. Create a generator that generates the squares of numbers up to some number `N`.
def n_squares(n):
    # return (i ** 2 for i in range(0, N + 1))
    i = 0
    while i <= n:
        yield i ** 2
        i += 1


# 2. Write a program using generator to print the even numbers between 0 and `n` in comma separated form where `n` is
# input from console.
def even_numbers(n):
    # return (i for i in range(0, N + 1) if i % 2 == 0)
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


# 3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4,
# between a given range 0 and `n`.
def div_by_3_and_4(n):
    # return (i for i in range(0, n + 1) if i % 3 == 0 and i % 4 == 0)
    i = 0
    while i <= n:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i -= 1


# 4. Implement a generator called `squares` to yield the square of all numbers from (a) to (b). Test it with a "for"
# loop and print each of the yielded values.
def squares(a, b):
    # return (i ** 2 for i in range(a, b + 1))
    i = a
    while i <= b:
        yield i ** 2
        i += 1


# 5. Implement a generator that returns all numbers from (n) down to 0.
def n_to_0(n):
    # return (i for i in range(n, -1, -1))
    i = n
    while i >= 0:
        yield i
        i -= 1