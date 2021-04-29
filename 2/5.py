from pprint import pprint

sentence = "This is a common interview question"

char_frequency: dict = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1)

# since we cannot sort a dictionary, im gonna convert them to tuples inside list and then sort them
print(sorted(
    char_frequency.items(),
    # key=lambda kv: kv[1],
    reverse=True
))
# char_frequency.items() returns key values in tuples inside one list, basically >>> [(k, v), (k, v)]!
