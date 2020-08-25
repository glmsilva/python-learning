import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# the test url -> http://py4e-data.dr-chuck.net/known_by_Fikret.html
# the assignment url -> http://py4e-data.dr-chuck.net/known_by_Gavin.html
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Enter the count: "))
pos = int(input("Enter position: ")) - 1

last_name = None

for i in range(count):

    tags = soup('a')
    #print(tags[pos])
    last_name = tags[pos].contents[0]
    #print(tags[pos].contents[0])
    montgomery = tags[pos].get('href', None)
    url = montgomery
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


print(last_name)
#for tag in tags:
    #print(tag.contents[0])


#montgomery = tags[pos].get('href', None)
#url = montgomery
#html = urllib.request.urlopen(url,context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

#tags2 = soup('a')
#print(tags2[2].contents[0])



