import urllib.request

import json 

req=urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos/1");
data = json.loads(req.read())


print(data)


