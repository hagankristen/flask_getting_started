import requests

def vm_requests():
    """tests GET and POST functions in mini2.py
    """
    r = requests.get("http://vcm-3580.vm.duke.edu:5000/name")
    print(r.json())
    name = "Kristen Hagan"
    r = requests.get("http://vcm-3580.vm.duke.edu:5000/hello/%s" % name)
    print(r.json())
    r = requests.post("http://vcm-3580.vm.duke.edu:5000/distance", json = {"a": [6,7], "b": [4,3]})
    print(r.json())
    r = requests.post("http://vcm-3580.vm.duke.edu:5000/distance", json = {"a": [1,1], "b": [1,1]})
    print(r.json())

if __name__ == '__main__':
    vm_requests()
