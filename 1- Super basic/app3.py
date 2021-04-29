def increment(number, by=99):
    return (number, number + by)


print(increment(number=2, by=3))  # (2, 5) - this is a tuple (read only list)
print(increment(2, 3))
print(increment(2))

# if you set default value, you can choose to not pass that arg!


def anotherIncrement(number: int, by: int = 1) -> tuple:
    return (number, number + by)

# ***********************************************
# xargs


def multiply(*list):  # * means py will package args to tuple
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# **********************************************
# xxargs


def save_user(**user):  # ** means py will package key value to something like object in javascript
    # user is like object in javascript, user["name"] is admin
    print(user["name"])

save_user(id=1, name="admin")

# **********************************************

message = "a"

   
def greet():
    global message
    message = "b"  # because of above line, the global var will get changed, otherwise message will be "b" only in this function!
