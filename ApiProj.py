import requests
import json

r = requests.get("http://bme590.suyash.io/list")
check = r.json()
print(check)
keh = {
        "first_name": "Kristen",
        "last_name": "Hagan",
        "netid": "keh73",
        "github_username": "hagankristen",
        "team_name": "LaserEye"
}
r2 = requests.post("http://bme590.suyash.io/student", json = keh)
