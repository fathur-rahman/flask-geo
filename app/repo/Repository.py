

from app import jsonifier
from app.jsonifier import *
from app.models.models import db
import uuid
from geoalchemy2 import shape as ga2shape 
from shapely.geometry import shape
 
class Repository:
    model = None 
    
    def get(self, id, return_as_json = False):
        obj = self.model.query.get(str(id))
        if not obj:
            raise Exception(f"Data {self.model.__name__} tidak ditemukan.")
        if return_as_json:
            return Jsonifier().obj_to_json(obj)
        return obj
        
    def store(self, req_json):
        newobj = self.model()

        newobj.id = str(uuid.uuid4())
        newobj = Jsonifier().json_to_object(newobj, req_json=req_json)


        db.session.add(newobj)
        db.session.commit()
        return newobj

    def update(self, id, req_json):
        obj = self.get(id = str(id))
        obj = Jsonifier().json_to_object(obj, req_json=req_json)
        db.session.commit()
        return obj