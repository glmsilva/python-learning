import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #http://py4e-data.dr-chuck.net/comments_903871.xml
jsurl = urllib.request.urlopen(url)
data = jsurl.read().decode()
js = json.loads(data)

soma = 0

for num in js["comments"]:
    soma += int(num["count"])

print(soma)