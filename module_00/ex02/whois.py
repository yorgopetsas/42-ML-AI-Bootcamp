import sys

x = sys.argv[1]

if (x.isdigit() is False):
    print("\nPlease provide a whole number. ", end='')
    print("No decimal separators, float nor strings allowed)\n")
    exit()
if int(x) == 0:
    print("\nThis is 0")
elif (int(x) % 2 == 0):
    print("\nThe number is Even\n")
else:
    print("\nThe number is Odd\n")
