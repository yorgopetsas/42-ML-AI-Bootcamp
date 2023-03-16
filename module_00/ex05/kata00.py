kata = (19, 42, 21)
print(f'The {len(kata)} numbers are: ', end='')
for i in range(len(kata) - 1):
    print(f'{kata[i]}, ', end='')
print(f'{kata[-1]}')
print()
