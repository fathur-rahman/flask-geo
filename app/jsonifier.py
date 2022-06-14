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
        json = {}

        for dict_attr in obj.__dict__:
            value = getattr(obj, dict_attr)
            if '_sa' in dict_attr: 
                continue

            if isinstance(value, datetime):
                value = datetime.strftime(value, format='%Y-%m-%d %H:%M:%S')

            if isinstance(value, float):
                value = int(value)

            if isinstance(value, WKBElement):
                value = mapping(ga2shape.to_shape(value))
            
            json[dict_attr] = value

        for all_attr in dir(obj):
            attrsplit= all_attr.split('_')
            fk_value = getattr(obj,all_attr)
            if 'detail' in attrsplit and '_' in all_attr:
                json[all_attr] = self.obj_to_json(fk_value) 
             
        return json
    
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