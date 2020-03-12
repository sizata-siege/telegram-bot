import requests
import re
url0 = 'http://m-taghizadeh.ir'
url1 = 'https://soft98.ir'
url2 = 'https://google.com'
response = requests.get(url2)
print(response.text)
emails = re.findall("[a-zA-Z0-9.]+@[a-zA-Z]+.[a-zA-Z]+", response.text)
print(emails)
title = re.findall("<title>[a-zA-Z0-9.]+</title>", response.text)
title = title[0]
print(title[7:-8])
