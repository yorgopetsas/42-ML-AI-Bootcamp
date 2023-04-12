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

prompt = ""

if len(sys.argv) < 2:
    print('\nError.Please provide at least one argument')

arg_cnt = len(sys.argv) - 1

for i, s in enumerate(sys.argv):
    arg_len = len(sys.argv[i])
    #Skip first argument
    if i == 0:
        continue
    for x, l in enumerate(s):
        #Check if alphanumeric or space
        if l != ' ' and l.isalnum() == False:
            print('Error')
            exit()
        prompt = prompt + l
        if x == len(s) - 1 and i < arg_cnt:
            prompt = prompt + " "
    
fnl_str = "".join(prompt)

for i in fnl_str:
    if i == ' ':
        print('/', end=' ')
    else:
        print(morse[i.upper()], end=' ')
print()





