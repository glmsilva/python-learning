import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# the test url -> http://py4e-data.dr-chuck.net/comments_42.html
# the assignment url -> http://py4e-data.dr-chuck.net/comments_903869.html
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


numbers = list()
soma = None

tags = soup('span')
for tag in tags:
    numbers.append(int(tag.contents[0]))

for num in numbers:
    if soma is None:
        soma = num 
    else: 
        soma += num

print(soma)