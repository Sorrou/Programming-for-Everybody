import re
file = open('D:\\ip.txt')

counts = dict()
for line in file:
    words = line.split()
    for word in words:
        if re.findall('[0-9.]+', word):
            counts[word] = counts.get(word, 0) + 1

print(counts)
