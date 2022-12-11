d1 = {"producer": "Dell","model": "Inspiron","year": 2017}
print ("producer:", d1["producer"])
print (d1)
d2 = {
    "producer": "Dell",
    "model": "Inspiron",
    "year": 2017,
    "colors": ["red", "white", "blue"]
    }
print ("colors: ", d2["colors"])
d2["producer"] = "Google Inc"
print ("producer: ", d2["producer"])
print (d2)
#3
import json
d3 = json.dumps(d2)
print (d3)
#4
from urllib.request import urlopen
url = "https://api.github.com"
response = urlopen(url)
data_json = json.loads(response.read())
print(data_json)