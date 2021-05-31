# COMMAND LINE ARGUMENTS

import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python3 10.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
