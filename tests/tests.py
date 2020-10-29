from app.app import (
    silly_request,
    url,
    auth,
    token_file_name,
    take_acess_token,
    token_file_name_in,
    link_toke_file,
)


def assert_silly_request(url):
    json_requested_error = silly_request(url)
    assert json_requested_error == {
        "message": "404: Not Found",
        "code": 0,
    }, json_requested_error


assert_silly_request(url)


def try_auth(token_file_name):
    received_response = auth(token_file_name)
    assert (
        received_response.status_code == 200
    ), f"resposta recebida: {received_response.status_code}"


try_auth(token_file_name)


def try_download_acess_token():

    result, result_status = take_acess_token(token_file_name_in, link_toke_file)

    assert result_status == "downloaded" or result_status == "local, not downloaded"
    assert result == "acess.token", result


try_download_acess_token()
