from app.take_auth import take_auth
from app.config import take_acess_token
import requests


url_base = "https://discord.com/api"
api_version = "latest"
url = url_base + "/" + "v" + {"latest": "8", "7": "7", "6": "6"}.get(api_version, "8")

# seting cofigurations from config.cfg
with open("config.cfg", "r") as config_file:
    confiuration_params = dict(
        [
            line.strip(" ").replace("\n", "").replace(" ", "").split("=")
            for line in config_file.readlines()
        ]
    )
    token_file_name_in = confiuration_params["token_file_name"]
    link_toke_file = confiuration_params["link_toke_file"]


token_file_name, status = take_acess_token(token_file_name_in, link_toke_file)


# print("URL definida: ",url)


def silly_request(url):
    """
    faz uma requisição get burra na url_base + versão
    exmp: https://discord.com/api/v8
    """
    # print("conect to ",url)
    requisição = requests.get(url)
    return requisição.json()


def auth(token_file_name):
    url = take_auth(token_file_name)
    print("taking auth with: ", url)
    return requests.get(url)


##########################testes

if __name__ == "__main__":
    print("1")
