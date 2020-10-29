from pprint import pprint

# def configure(API_ENDPOINT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI):


def take_auth(token_file_name):
    """expected a file with 3 lines without spaces like:

    client_id=999999999999999999
    scope=bot
    permisions=9

    """

    with open(token_file_name, "r") as token_file:
        params = dict(
            [
                line.strip(" ").replace("\n", "").replace(" ", "").split("=")
                for line in token_file.readlines()
            ]
        )

    url = "https://discord.com/api/oauth2/authorize?"

    # print(params["permisions"])
    client_id = params["client_id"]
    scope = params["scope"]
    permissions = params["permisions"]

    return f"{url}client_id={client_id}&scope={scope}&permissions{permissions}"


#   https://discord.com/api/oauth2/authorize?client_id=157730590492196864&scope=bot&permissions=1
