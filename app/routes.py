from app import app
from flask_restful import Api
from app.controller.DataController import DataController

def init_routes(app):
    web = Api(app)
    web.add_resource(DataController,'/data','/data/<string:id>')
