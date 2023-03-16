from datetime import datetime

kata = (2019, 9, 25, 3, 30)

data = ''
for i in range(len(kata)):
    data = data + str(kata[i])

result = datetime.strptime(data, "%Y%m%d%H%M")

print(result.strftime("%m/%d/%Y %H:%M"))
