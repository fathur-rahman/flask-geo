from dataclasses import asdict
import json

from flask import jsonify
from app.models.models import db
import uuid
 
class Repository:
    model = None 
    
    def get(self, id, return_as_json = False):
        data = self.model.query.get(id)

        if not data:
            raise Exception(f"Data {self.model.__name__} tidak ditemukan.")
        # print(data)
        return {"id":data.id, "name":data.name, "geometry":data.geometry}

        
    def store(self, req_json):
        newobj = self.model()
        # newobj.id = str(uuid.uuid4())
        # newobj.name = req_json.get('name')
        # self.model.geometry = req_json.get('geometry')
        for key, value in req_json.items():
            setattr(self.model, str(key), value)

        db.session.add(newobj)
        db.session.commit()
        return newobj

        # return self.query.store(obj)
    def update(self, req_json):
        for key, value in req_json:
            setattr(self.model(), key, value if key in req_json else getattr(self.model(), key))