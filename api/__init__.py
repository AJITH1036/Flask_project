from flask_restful import Api
from app import app
from .user import *
from . product import *

api = Api(app)
api.add_resource(User,'/api/users/')
api.add_resource(UserEdit,'/api/users/<int:user_id>')
api.add_resource(Products,'/api/products/')
api.add_resource(EditProducts,'/api/products/<int:pid>')

api.init_app(app)