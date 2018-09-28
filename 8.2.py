fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for i in fh:
    a = i.rstrip()
    if a.startswith('From'):
        if a.startswith('From:'):
            continue
        print(a.split()[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
