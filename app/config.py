import requests
import os
import os.path


def take_acess_token(file_name, link_toke_file):
    """"""

    if os.path.isfile(file_name):
        return file_name, "local, not downloaded"

    with open(file_name, "wb") as acess_token_file:
        try:
            acess_token_file.write(requests.get(link_toke_file).content)
        except Exception as e:
            acess_token_file.close()
            os.remove(file_name)
            raise Exception("link_toke_file in config.cfg is invalid\nit is like")
        else:
            ...
            # return file_name, "downloaded"
    return file_name, "downloaded"

    raise Exception(f"erro inesperado durante execução de {take_acess_token.__name__} ")
