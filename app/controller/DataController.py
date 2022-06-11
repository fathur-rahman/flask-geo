from app.response import *
from flask import jsonify, request
from flask_restful import Resource
import traceback
from app.models.models import BE_PYTHON
from app.repo.DataRepository import DataRepository
class DataController(Resource):
    def get(self, id=None):
        try:
            if id:
                return DataRepository().get(id)
            else:
                return DataRepository().getAll()
        except Exception as e:
            print(traceback.format_exc())
            return badRequest('','{}'.format(e))


    def post(self):
        try:
            data = DataRepository().store(request.json)   
            data = DataRepository().get(id = str(data.id))
            # data = DataRepository().get(id = str(data.id), return_as_json=True)

            return data
        except Exception as e:
            print(traceback.format_exc())
            return badRequest('','{}'.format(e))

    def patch(self, id):
        try:
            return "patch Hello, World!"        
            print('post')
        except Exception as e:
            print(traceback.format_exc())
            return badRequest('','{}'.format(e))