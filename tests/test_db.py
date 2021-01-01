import sqlite3
import pytest
from testapp.db import get_db

def test_get_close_db(app):
    # should return same connection each time in app context
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECt 1')

    assert 'closed' in str(e.value)


def test_init_db_command(runner, monkeypatch):
    # use pytests monkeypatch to replace init db func 
    # with another that records that it was called with
    # the Recorder class
    # the runner fixture in above func calls the init-db command

    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True
    
    monkeypatch.setattr('testapp.db.init_db',fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'initialized db' in result.output
    assert Recorder.called




    