import re


text = open('C:\\Users\\dachevich.v\\Documents\\audit.log.2018-10-16.txt', encoding='UTF-8')
#a = re.findall('[0-9]+', text)teln
for i in text.readlines():
    if "zubova" in i.split()[8]:
        print(i.split()[4])


#b = 0
#for i in a:
#    b += int(i)

#print(b)
