import random

def shuffle_words(words):
    new_words = []
    index = random.randint(0, len(words) - 1)
    while words:
        new_words.append(words[index])
        words.remove(words[index])
        if not len(words):
            index = 0;
        else:
            index = random.randint(0, len(words) - 1)
    return new_words

def generator(text, sep=' ', option=None):
    word = ''
    words = []

    for i in text:
        if i != sep:
            word = word + i
        else:
            words.append(word)
            word = ''
    print(words)
    if option == 'ordered':
        words = sorted(words)
    elif option == 'unique':
        words = list(dict.fromkeys(words))
    elif option == 'shuffle':
        words = shuffle_words(words)
    for x in words:
        yield x
    exit()

text = "wer Le Lorem le Le LE le Ipsum est simplement est du faux texte."

# List the words as separate arrays
# for word in generator(text, sep=' '):
#     print(word)

# List the words as separate arrays ordered alphabetically
# for word in generator(text, sep=' ', option='ordered'):
#     print(word)

# List only the unique words as separate arrays
# for word in generator(text, sep=' ', option = 'unique'):
#     print(word)

# List the words as separate arrays in random order
# for word in generator(text, sep=' ', option = 'shuffle'):
#     print(word)
