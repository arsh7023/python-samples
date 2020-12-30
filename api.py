import urllib.request, json

response= urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos/1")
data = json.loads(response.read())

print(data)
 
