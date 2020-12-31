from testapp import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING':True}).testing

def test_ok(client):
    response = client.get('/ok')
    assert response.data == b'ok'