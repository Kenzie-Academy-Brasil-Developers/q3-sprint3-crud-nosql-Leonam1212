from flask import Flask

# from .views import posts as posts_view

from app import routes

def create_app():

    app = Flask(__name__, static_folder=None)
    routes.init_app(app)
    # posts_view.init_app(app)

    return app