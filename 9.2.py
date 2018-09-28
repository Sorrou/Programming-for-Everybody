name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
dct = dict()
lst = list()

for i in handle:
    if i.startswith('From '):
        h = i.split()[5]
        h2 = h.split(':')[0]
        if h2 not in dct:
            dct[h2] = 1
        else:
            dct[h2] = dct[h2] + 1

for k, v in dct.items():
    lst.append((k, v))

for val in sorted(lst):
    print(*val)
