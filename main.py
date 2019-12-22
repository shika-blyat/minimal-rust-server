import requests

r =requests.get('http://localhost:8000/hello/world')
print("response was:" + r.text)