# def configure(API_ENDPOINT, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI):

def take_auth(token_file_name):
    """expected a file with 3 lines without spaces like:
        
        client_id=999999999999999999
        scope=bot
        permisions=9

    """



    with open(token_file_name,'r') as token_file:
        lines = token_file.readlines()
        
    url =  "https://discord.com/api/oauth2/authorize?"
    client_id = lines[0].strip()
    scope = lines[1].strip()
    permissions = lines[2].strip()

    return f"{url}{client_id}&{scope}&{permissions}"
  

#   https://discord.com/api/oauth2/authorize?client_id=157730590492196864&scope=bot&permissions=1
