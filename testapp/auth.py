import functools
from flask import (
    Blueprint, flash, g, 
    redirect, render_template, request, 
    session, url_for
)
from werkzeug.security import (
    check_password_hash, generate_password_hash
)

from .db import get_db

bp = Blueprint('auth',__name__, url_prefix='/auth')


@bp.route('/register',methods=('GET','POST'))
def register():
    # check if user is registering and if username exists already
    # db library takes care of escaping apparently??
    # store error messages as well
    # 

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'need a username'
        elif not password:
            error = 'need a password'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'already registered'

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

            
        flash(error)


    return render_template('auth/register.html')


@bp.route('/login', methods = ('GET','POST'))
def login():
    # query user and securely compare password hashes
    # store data in a cookie with session dict
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?',
            (username,)
        ).fetchone()

        if user is None:
            error = 'incorrect username'
        elif not check_password_hash(user['password'],password):
            error = 'incorrect password'
        
        if error is None:
            session.clear()
            session['user_id']= user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    # for any URL, if user is presently logged in 
    # have the data associated with the user readily availabe
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?',
            (user_id,)
        ).fetchone()


@bp.route('/logout')    
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    # decorator that returns a new view function that is
    # warpped to the original view.
    # sends the user back to login if they get logged out


    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

