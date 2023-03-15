import sys
import string


if (len(sys.argv)) < 2:
    print("This command requiers at least one argument and you provided 0")
input = ' '.join(sys.argv[1::])[::-1].swapcase()
print(input)
