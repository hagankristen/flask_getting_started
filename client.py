import requests

r = requests.get("http://vcm-3580.vm.duke.edu:5000/name")
print(r.json())
name = "Kristen Hagan"
r = requests.get("http://vcm-3580.vm.duke.edu:5000/hello/%s" % name)
print(r.json())
r = requests.post("http://vcm-3580.vm.duke.edu:5000/distance", json = {"a": [6,7], "b": [4,3]})
print(r.json())
r = requests.post("http://vcm-3580.vm.duke.edu:5000/distance", json = {"a": [1,1], "b": [1,1]})
print(r.json())
