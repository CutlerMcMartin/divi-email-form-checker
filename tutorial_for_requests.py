import requests

payload = {'page': 2, 'count': 25}

r = requests.post('https://httpbin.org/post', params=payload)

print(r.url)