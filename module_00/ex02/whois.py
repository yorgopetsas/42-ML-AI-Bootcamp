import sys


def whois(x):

    if (x.isdigit() is False):
        print("\nPlease provide a whole number. ", end='')
        print("No decimal separators, float nor strings allowed\n")
        exit()
    if int(x) == 0:
        print(f"\nThe number {x} is Even.")
    elif (int(x) % 2 == 0):
        print(f"\nThe number {x} is Even.")
    else:
        print(f"\nThe number {x} is Odd.")

if len(sys.argv) < 2:
    x = input("\nPlease provide a number: ")
    print(x)
    whois(x)

elif len(sys.argv) > 2:
    x = input("\nPlease provide only one number: ")
    whois(x)

else:
    x = sys.argv[1]
    whois(sys.argv[1])
