import requests

endpoint_url = "http://127.0.0.1:8000/product/"
resp = requests.get(endpoint_url, params={"abc": 123}, json={"query": "test"})
print(resp.text)