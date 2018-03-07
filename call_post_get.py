import requests


r = requests.get("http://127.0.0.1:5000/name")
print(r.json())
name = "Kristen Hagan"
r = requests.get("http://127.0.0.1:5000/hello/%s" % name)
print(r.json())
r = requests.post("http://127.0.0.1:5000/distance", json = {"a": [6,7], "b": [4,3]})
print(r.json())
