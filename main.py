
from urllib import request

url = "http://official-joke-api.appspot.com/jokes/ten"
req = request.urlopen(url)

print(req.getcode())
print(req.read())


