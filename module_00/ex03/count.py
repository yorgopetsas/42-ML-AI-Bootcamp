import sys
import string


def text_analyzer():
    x = sys.argv[1]
    print(f'\nThe text is {len(x)} caracter(s) long')
    up = lo = pu = 0

    for c in x:
        if c.isupper():
            up = up + 1
        elif c.islower():
            lo = lo + 1
        elif c in string.punctuation:
            pu = pu + 1
        elif c == " ":
            s = s + 1
    print(f'{lo} Lower case letters\n{up} Upper case letters\n{pu} Puntions\n')


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: More then 1 argument")
        exit()

    elif len(sys.argv) > 1:
        text_analyzer()

    else:
        print("\nPlease provide at least 1 argument\n")
