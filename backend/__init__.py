from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config# we’ll discuss the config file next
from backend.db import db



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")


    db.init_app(app)

    from backend.users.controller import users
    #registering blueprints    
    app.register_blueprint(users,url_prefix='/users')
  

   
    return app