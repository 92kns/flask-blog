import os
from flask import Flask

# create the application factory 

def create_app(test_config=None):
    # TODO add typing for inarg
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path,'testapp.sqlite'),
        )
    
    if not test_config:
        # load instance config
        app.config.from_pyfile('config.py',silent=True)
    else:
        # load test 
        app.config.from_mapping(test_config)

    # check instance exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # dev page
    @app.route('/ok')
    def ok():
        return 'cakey'


    # for app registration

    from . import ( db, auth, blog )
    
    db.init_app(app)

    app.register_blueprint(auth.bp)


    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
