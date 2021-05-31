x = input("x: ")

# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy >>>
# ""
# 0
# []
# None

# if 1 > 2:
#     print("ABC")
# elif 2 > 2:
#     print("Hello")
# else:
#     print("sfnslfks")

# print("All done!")


# if 0 > 0:
#     pass  # just a keyword that does nothing
# else:
#     print("ok")

name = ""
if not name.strip():
    print("Name is empty")


age = 22
if age >= 18 and age < 65:
    pass
# another way to write that ^ >>>
if 18 <= age < 65:
    pass

# ternary operator >>>
message = "Eligible" if age >= 18 else "Not eligible"

# ******************************************
for x in "Python":
    pass

for x in ['a', 'b']:
    pass

for y in range(5):  # 0 till 4
    pass

for y in range(2, 5):  # 2 till 4
    pass

for y in range(0, 10, 2):  # 3rd arg is step, result is 0 2 4 6 8
    pass

print(range(5))
# result is range(0,5) => doesn't return list, rather this thing is from class "range"

# range doesn't take a lot of memory even range(500000000) as opposed to 5 billion items in list

# ******************************************

# for...else
# names = ["John", "Mary"]

# for name in names:
#     if name.startswith("J"):
#         print("Found")
#         break
# else:
#     print("Not found")

# while loop >>>

guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:
    pass
