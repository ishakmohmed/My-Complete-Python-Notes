# Arrays
from array import array

numbers = array("i", [1, 2, 3])
# first arg is typecode

# SETS (we cannot access them using index)
nums = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4}
second.add(5)
second.remove(5)

one = set([1, 1, 2, 3, 4])
two = {1, 5}

print(one | two)
print(one & two)
print(one - two)
print(one ^ two)

# Dictionary
point = {
    "x": 1,
    "y": 2
}

anotherPoint = dict(x=1, y=2)

point["x"] = 10
point["abc"] = 20
# just like in js, if key doesn't exist it's gonna add it with value

if "a" in point:
    print(point["a"])

# a better way ^ >>>

print(point.get("a", 0))
# 2nd OPTIONAL arg is default return value

del point["x"]

for key in point:
    print(key, point[key])

# or

for key, value in point.items():
  # point.items() will become a tuple
    print(key, value)

# ****************************
# DICTIONARY COMPREHENSION

# [expression for item in items]
# you can do this for lists, dictionaries, sets, (NOT FOR TUPLES)

values = {x: x * 2 for x in range(5)}
# the only difference is that now it's in curly braces (and now we've got key value).
