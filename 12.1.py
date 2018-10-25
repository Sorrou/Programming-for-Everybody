from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
count = 1
for tag in tags:
    if count == 19:
        break
    print('count = ', count, tag.get('href', None))
    count += 1


#1 http://py4e-data.dr-chuck.net/known_by_Deacon.html
#2 http://py4e-data.dr-chuck.net/known_by_Prabhjot.html
#3 http://py4e-data.dr-chuck.net/known_by_Matas.html
#4 http://py4e-data.dr-chuck.net/known_by_Ocean.html
#5 http://py4e-data.dr-chuck.net/known_by_Penny.html
#6 http://py4e-data.dr-chuck.net/known_by_Zhuo.html
#7 http://py4e-data.dr-chuck.net/known_by_Radmiras.html