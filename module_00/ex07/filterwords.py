import sys
import string


if len(sys.argv) == 3:
    text = sys.argv[1]
    try:
        limit = int(sys.argv[2])
    except Exception:
        print("Second Argument not an Integer")
    word = ''
    for i in text:
        if i in string.punctuation:
            continue
        elif i is ' ':
            if len(word) > limit:
                print(word)
                word = ''
                continue
            else:
                word = ''
                continue
        word = word + i
        # print(word)
    if len(word) > limit:
        print(word)

else:
    print('AssertionError: wrong number of arguments')
