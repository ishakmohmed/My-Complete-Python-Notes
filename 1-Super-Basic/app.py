# primitives are immutable!

import math
xyz = """ 
multiple
lines
"""

x, y = 1, 2
print(id(x))

print(type(x))

age: int = 20  # needa use mypy to enable type checking

# *********************************************************
# strings are immutable!
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])  # last charater - g!
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

first = "Mohmed"
last = "Ishak"
full = f"{len(first)} {last}"  # formatted string: prefix w f or F

course.upper()
course.lower()
course.title()
course.strip()  # white space start/end
course.rstrip()
course.lstrip()
course.find("Pro")  # case sensitive
course.replace("P", "-")

print("Programming" in course)  # true
print("Programming" not in course)  # false

# ****************************************************
x = 0b10  # means 2 - binary
print(bin(5))  # returns binary representation

x = 0x12c  # hexadecimal
print(hex(x))

abc = 10 / 3  # float
abc = 10 // 3  # int
abc = 10 ** 3  # exponent

# there's no x++ or x-- in python

# ****************************************************
PI = 3.14
print(round(PI))
print(abs(PI))

math.floor(PI)

