handle = open('D:\\mail.txt', 'r')
lst = list()
dct = dict()

for i in handle:
    if i.startswith('From '):
        lst.append(i.split()[1])

for a in lst:
    if a not in dct:
        dct[a] = 1
    else:
        dct[a] = dct[a] + 1

max = max(dct.values())

for key, value in dct.items():
    if value == max:
        print(key, value)
