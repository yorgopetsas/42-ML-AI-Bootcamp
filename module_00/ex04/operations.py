import sys

if (len(sys.argv) != 3):
    print("\nError: Please provide exactly 2 numbers. No other input accepted!\n\nUsage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3\n")

elif (sys.argv[1].isdigit() and sys.argv[2].isdigit()) and (len(sys.argv) == 3) or (sys.argv[1][0] == "-" or sys.argv[2][0] == "-" and sys.argv[1][1::].isdigit() and sys.argv[2][1::].isdigit()):
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(f'Difference is {a - b}')
    print(f'Product is {a * b}')
    if int(b) == 0:
        print("Quotient: ERROR (division by zero)\nRemainder: ERROR (division by zero)")
    else:
        print(f'Quotient is {a / b}')
        print(f'Remainder is {a % b}')