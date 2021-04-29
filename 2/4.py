# generator expressions- generator objects don't store stuffs in memory, rather they generate stuffs and allocate stuffs in every iteration

from sys import getsizeof

values = (x * 2 for x in range(100000))
# ^ this is a generator object cause it is surrounded by parantheses (tuple?)
print("gen:", getsizeof(values))
# size will be small and consistent if its for a range of 100 or 1000000, unlike the same thing but surrounded by square brakcets which will allocate a lot of memory


# UNPACKING OPERATOR (* basically the spread operator in javascript)

numbers = [1, 2, 3]
print(*numbers)
# result is 1 2 3 no brackets, no commas, just plain numbers

# you can unpack any iterables!
vals = [*range(5), *"Hello"]

# you can unpack objects too but use two asterisk ** and >>>

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second}
# here, "x" will get overridden