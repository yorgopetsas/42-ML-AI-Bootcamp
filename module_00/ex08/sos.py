import sys
import string


morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '· − − − − ·',
    '!': '− · − · − −',
    '/': '− · · − ·',
    '(': '− · − − ·',
    ')': '− · − − · −',
    '&': '· − · · ·',
    ':': '− − − · · ·',
    ';': '− · − · − ·',
    '=': '− · · · −',
    '+': '· − · − ·',
    '-': '− · · · · −',
    '_': '· · − − · −',
    '"': '· − · · − ·',
    '$': '· · · − · · −',
    '@': '· − − · − ·',
}

prompt = []

if len(sys.argv) < 2:
    print('\nError.Please provide at least one argument')

for i, l in enumerate(sys.argv):
    for x, l in enumerate(sys.argv[i]):
        print(x)
        if i == 0:
            continue
        if l == " ":
            prompt.append(l)
        elif l.isalnum():
            prompt.append(l)
        
        # else:
        #     print(prompt)
        #     exit()

    arg_len = len(sys.argv[i])
    if arg_len > x + 1:
        print('end')
    print(arg_len)
    # print(i)
    if i > 0:
        prompt.append(" ")
    print(prompt)

jtext = "".join(prompt)

for i in jtext:
    if i == ' ':
        print('/', end=' ')
    else:
        print(morse[i.upper()], end=' ')
print()
