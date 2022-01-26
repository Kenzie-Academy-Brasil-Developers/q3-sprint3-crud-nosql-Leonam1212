# Retorno das rotas
from flask import Flask

def init_app(app: Flask):
    from app.routes.post_route import post_routes
    post_routes(app)