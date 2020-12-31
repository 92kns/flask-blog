import sqlite3
import click
from flask import (current_app, g)
from flask.cli import with_appcontext

def get_db():
    # connection func

    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        # let's get some rows as dict like structures
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # close func
    db = g.pop('db',None)

    if db is not None:
        db.close()

    pass

def init_db():
    # to run schema queries

    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    pass

@click.command('init-db')
@with_appcontext
def init_db_command():
    # re-initialize db
    init_db()
    click.echo('Initialized DB!')
    pass

# register application 
# since we are using a factory function

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

    pass















