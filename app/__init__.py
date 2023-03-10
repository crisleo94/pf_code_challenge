from flask import Flask

from .models import db
from .models.factory import Factory
from .models.sprocket import Sprocket
from .routes import api

app = Flask(__name__)

def create_app(environment):
    app.config.from_object(environment)

    app.register_blueprint(api)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
