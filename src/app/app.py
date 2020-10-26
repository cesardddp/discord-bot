import requests

print("aaaa")

url_base =  "https://discord.com/api"
api_version = "latest"
url = url_base + 'v' + {"latest":"8","7":"7","6":"6"}.get(api_version,"8")

requisição = requests.get(url)
print(requisição.status_code)