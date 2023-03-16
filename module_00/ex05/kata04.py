from decimal import Decimal

kata = (11, 4, 132.42222, 10000, 12345.67)

if kata[0] < 10:
    print(f'module_0{kata[0]}', end=', ')
else:
    print(f'module_{kata[0]}', end=', ')
if kata[1] < 10:
    print(f'ex_0{kata[1]}', end=' : ')
else:
    print(f'ex_{kata[1]}', end=' : ')
print(round(kata[2], 2), end='')

for i in range(2):
    data = kata[3 + i]
    data = Decimal(data)
    print(", %.2E" % data, end='')
