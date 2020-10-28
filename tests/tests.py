from app.app import silly_request,url
def assert_silly_request(url):
    json_requested_error = silly_request(url)
    assert json_requested_error == {'message': '404: Not Found', 'code': 0}, json_requested_error
assert_silly_request(url)

from app.app import auth,token_file_name
def try_auth(token_file_name):
    received_response = auth(token_file_name)
    
    assert received_response.status_code == 200
try_auth(token_file_name)