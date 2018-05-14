from flask import Flask
from config import config_options

def create_app(config_name):
    '''
    Initializing our app
    '''

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .request import configure_request
    configure_request(app)
    


    return app


