letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
# combined = zeros + letters # works on Mosh's machine but not mine, idk why.

# numbers = list(range(20))
print(list(range(20)))
print(list("Hello world"))
# ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# apply len() to calculate the length of these 2

print(letters[0:3])
print(letters[::2])
# 2 here is step which is optional, you can pass -1 too so it'll move from back one step at a time!

# list unpacking >>>
numbers = [1, 2, 3]
first, second, third = numbers
# ^ so second is 2 (pass exact variables or >>>)

anotherNumbers = [1, 2, 3]
first, *other = anotherNumbers
print(first)
# ^ 1
print(other)
# ^ [2, 3]

# what if you care about first and last item only?
items = [1, 2, 3, 4, 4, 9]
first, *other, last = items
print(first, last)
print(other)

for letter in enumerate(letters):
    pass
# enumerate will return a tuple (0, "a"), so index first and then the actual item

# or you can >>>
for index, alphabet in enumerate(letters):
    print(index, alphabet)
# with this we can unpack index, alphabet from the tuple

# *********************************************

stuffs = ["a", "b", "c", "d", "e", "c", "c", "c", "c"]

stuffs.append("f")
stuffs.insert(5, "asld")
stuffs.pop()
stuffs.pop(0)
stuffs.remove("b")
# only the first b will be removed
del stuffs[0]
del stuffs[0:3]
stuffs.clear()

if "c" in stuffs:
    stuffs.index("c")
    # if doenst exist, it wouldnt return -1, so needa if check

stuffs.count("c")

# *********************************************
numbers = [3, 51, 2, 8]
numbers.sort(reverse=True)
# will modify actual numbers
sorted(numbers, reverse=True)
# return new stuffs

# what if you wanna sort complex stuffs ?
things = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12),
]


# def sort_item(item):
#     return item[1]

#     things.sort(key=sort_item)

# a better way by using lambda functions >>>

things.sort(key=lambda item: item[1])
# (key=lambda parameter:expression)