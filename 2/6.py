try:
    age = int(input("Age: "))
except ValueError as ex:
    # as ex is optional
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions")
# else is optional


#  ********************************

try:
    file = open("1.py")
    age = int(input("Age: "))
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
finally:
    file.close()

#  ********************************

# you can use the "with" statement if a thing has context management protocol (has enter and exit magic method or something like that)

try:
    with open("1.py") as file:
        # now we don't need the file.close() cause python will automatically do that with "with" statement
        print("File opened")
    age = int(input("Age: "))
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")

#  ********************************

# raising exceptions - not recommended because it'll take a long time


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less!")
        # instead of raising, it's better to pass None
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
