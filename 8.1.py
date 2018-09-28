fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    if line.rstrip().split() not in lst:
        lst = lst + (line.rstrip().split())
lst.sort()
lst2 = list()
for i in lst:
    if i not in lst2:
        lst2.append(i)
print(lst2)
