fname = input("Enter file name: ")
fh = open(fname)
sm = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    stp = line.find(':')
    fp = float(line[stp + 1:])
    sm = sm + fp
    count += 1

print('Average spam confidence:', sm / count)
