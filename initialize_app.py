import os
from flask import Flask

def get_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('db_url','sqlite:///cat_pictures1.db')
    return app