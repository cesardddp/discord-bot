import requests
from app.take_auth import take_auth


url_base =  "https://discord.com/api"
api_version = "latest"
url = url_base + '/' + 'v' + {"latest":"8","7":"7","6":"6"}.get(api_version,"8")
token_file_name = "acess.token"

print("URL definida: ",url)

def silly_request(url):
    print("conect to ",url)
    requisição = requests.get(url)
    return requisição.json()

def auth(token_file_name):
    return requests.get(take_auth(token_file_name))
##########################testes

if __name__ == "__main__":
    print('1')