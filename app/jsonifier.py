from datetime import datetime
import json, geojson
from app import db
from geoalchemy2 import WKBElement
from geoalchemy2 import shape as ga2shape
from shapely.geometry import mapping, shape
class Jsonifier():

    def jsonifier(self, obj):
        if isinstance(obj, list):
            return list(map(self.obj_to_json, obj))

        return map(self.obj_to_json, obj)

    def obj_to_json(self, obj):
        x = {}

        for attr in obj.__dict__:
            z = getattr(obj, attr)
            if '_sa' in attr: 
                continue

            if isinstance(z, datetime):
                z = datetime.strftime(z, format='%Y-%m-%d %H:%M:%S')

            if isinstance(z, float):
                z = int(z)

            if isinstance(z, WKBElement):
                z = mapping(ga2shape.to_shape(z))
            
            x[attr] = z

        for attributes in dir(obj):
            a= attributes.split('_')
            zaa = getattr(obj,attributes)
            if 'detail' in a and '_' in attributes:
                x[attributes] = self.obj_to_json(zaa) 
             
        return x
    
    def json_to_shape(self, json):
        x = ga2shape.from_shape(shape(json))
        return x

    def json_to_object(self, obj, req_json):
        for key, value in req_json.items():
            if not isinstance(value, dict):
                setattr(obj, str(key), value)
            elif 'coordinates' in value or 'geometry' in value:
                setattr(obj, str(key), Jsonifier().json_to_shape(value) )
        return obj