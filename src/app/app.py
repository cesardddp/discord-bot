import requests

print("aaaa")

url_base =  "https://discord.com/api"
api_version = "latest"
url = url_base + '/' + 'v' + {"latest":"8","7":"7","6":"6"}.get(api_version,"8")

def silly_request(url):
    print("conect to ",url)
    requisição = requests.get(url)
    return requisição.json()


##########################testes

def assert_silly_request(url):
    json_requested_error = silly_request(url)
    assert json_requested_error == {'message': '404: Not Found', 'code': 0}, json_requested_error
assert_silly_request(url)