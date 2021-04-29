from collections import deque
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
]
# LIST COMPREHENSION => [expression for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
# without the list(), you'll only get a filter object

# rewriting using list comprehensions >>>
filtered = [item for item in items if item[1] >= 10]

# ************************************************

prices = list(map(lambda item: item[1], items))
# without the list() you'll only get a map object

# rewriting using LIST COMPREHENSIONS >>>
prices = [item[1] for item in items]

# ************************************************

# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list(zip(list1, list2))
# without list(), we'll only get zip object
# we'll get [(1, 10), (2, 20), (3, 30)]
list(zip("abc", list1, list2))
# you can pass "abc" here because it's an iterable
# we'll get [(a, 1, 10), (b, 2, 20), (c, 3, 30)]

# ************************************************


queue = deque([0])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
# result: deque([1, 2, 3])

# ************************************************
# tuple is a READ ONLY LIST LIST LIST LIST LIST LIST LIST LIST LISSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTTTTT !!!!!!!!!

point = 1, 2  # without parantheses, python will think that this is a tuple, empty parantheses means empty tuple

(1, 2) + (1, 2)
(1, 2) * 100
print(tuple("PASS ANYTHING ITERABLE HERE"))

# you can unpack tuples
x, y = point

# you can
point[0:1]

# ************************************************

x = 1
y = 2
# swapping variables >>>
x, y = y, x
# internally it'll convert it to tuple so x, y = (2, 1)