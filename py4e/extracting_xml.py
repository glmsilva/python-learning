import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #http://py4e-data.dr-chuck.net/comments_903871.xml
xml = urllib.request.urlopen(url, context=ctx).read()
data = xml.decode()
#print(data)
tree = ET.fromstring(data)
#print(tree)
lst = tree.findall('comments/comment')

soma = 0

for tag in lst:
    count = tag.find('count').text
    #print(count)
    soma += int(count)

print(soma)