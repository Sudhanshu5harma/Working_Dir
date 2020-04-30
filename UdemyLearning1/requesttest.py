import requests
import os


r = requests.get("http://google.com")
print("status: ", r.status_code)

filename= open("./page.html", "w")

filename.write(r.text)