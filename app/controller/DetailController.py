from app import response
from app.response import *
from flask import jsonify, request
from flask_restful import Resource
import traceback
from app.models.models import BE_PYTHON
from app.repo.DetailRepository import DetailRepository
class DetailController(Resource):
    def get(self, id=None):
        try:
            if id:
                data = DetailRepository().get(id, return_as_json = True)
            else:
                data =  DetailRepository().getAll()
            return response.ok(message=f"Berhasil mendapatkan{' seluruh' if not id else ''} data.", values =data)
        except Exception as e:
            print(traceback.format_exc())
            return badRequest('','{}'.format(e))


    def post(self):
        try:
            data = DetailRepository().store(request.json)
            data = DetailRepository().get(id = str(data.id), return_as_json=True)

            return response.ok(message="Berhasil menambahkan data.", values =data)
        except Exception as e:
            print(traceback.format_exc())
            return badRequest('','{}'.format(e))

    def patch(self, id):
        try:
            data = DetailRepository().update(id = str(id), req_json=request.json)   
            data = DetailRepository().get(id = str(id), return_as_json=True)
            return response.ok(message="Berhasil mengubah data.", values =data)
        except Exception as e:
            print(traceback.format_exc())
            return badRequest('','{}'.format(e))