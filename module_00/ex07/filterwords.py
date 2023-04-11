import sys
import string


if len(sys.argv) == 3:
    text = sys.argv[1]
    text_len = len(text)
    try:
        limit = int(sys.argv[2])
    except Exception:
        print("Second Argument not an Integer")
    words = []
    word = ''
    for i, l in enumerate(text):
        if l in string.punctuation:
            continue
        elif l == ' ':
            if len(word) > limit:
                words.append(word)
                word = ''
                continue
            else:
                word = ''
                continue
        word = word + l
        if i == text_len - 1 and len(word) > limit:
            words.append(word)
    print(words)

else:
    print('AssertionError: wrong number of arguments')
