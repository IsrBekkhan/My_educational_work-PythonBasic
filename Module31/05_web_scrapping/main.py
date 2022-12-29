import requests
from re import findall


my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
result = findall(r'<h3 id=".+>(.+)</h3>', my_req.text)
print(result)
