

from flask import jsonify
from app.jsonifier import jsonifier
from app.models.models import db
import uuid
 
class Repository:
    model = None 
    
    def get(self, id, return_as_json = False):
        data = self.model.query.get(id)
        if not data:
            raise Exception(f"Data {data.__name__} tidak ditemukan.")

        if return_as_json:
            data = jsonifier(data)
        return data
        
    def store(self, req_json):
        newobj = self.model()
        newobj.id = str(uuid.uuid4())
        for key, value in req_json.items():
            setattr(newobj, str(key), value)

        db.session.add(newobj)
        db.session.commit()
        return newobj

    def update(self, req_json):
        for key, value in req_json:
            setattr(self.model(), key, value if key in req_json else getattr(self.model(), key))