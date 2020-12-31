import os
import tempfile
import pytest
from testapp import create_app
from testapp.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    # point to tmp file
    # then insert test data
    # then close everything when done
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
            'TESTING':True,
            'DATABASE':db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions:
    # fake login for tests
    def __init__(self, client):
        self._client = client

    def login(self, username='t', password = 't'):
        return self._client.post(
            '/auth/login',
            data = {
                'username':username,
                'password':password
            }
        )
    
    def logout(self):
        # redirect to logout
        return self._client.get('/auth/logout')

# instantiate and return AuthAction object
# with an auth fixture
@pytest.fixture
def auth(client):
    return AuthActions(client)