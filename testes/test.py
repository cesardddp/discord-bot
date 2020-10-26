
def assert_silly_request(url):
    assert app.silly_request(url) == {'message': '404: Not Found', 'code': 200}

assert_silly_request(app.url)