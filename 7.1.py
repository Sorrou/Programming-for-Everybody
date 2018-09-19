smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)


numbs = []
while True:
    try:
        num = input()
        if num == "done":
            break
        else:
            num = int(num)
            numbs.append(num)
    except ValueError:
        print('Invalid input')

print("Maximum is", max(numbs))
print('Minimum is', min(numbs))
