import random
import string

random.random
random.randint(1, 100)
random.choice([1, 2, 3, 4])
random.choices([1, 2, 3, 4], k=2)

# gonna generate random password >
"".join(random.choices(string.ascii_letters + string.digits, k=4))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
# this will shuffle the original list
print(numbers)
