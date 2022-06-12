from datetime import datetime
import json, geojson
# import geoalchemy2
from geoalchemy2 import WKBElement
from geoalchemy2 import shape 
from shapely.geometry import mapping

class jsonifier():
    def jsonifier(self, obj):
        if isinstance(obj, list):
            return list(map(self.singular_jsonifier, obj))
        else:
            return self.singular_jsonifier(obj)

    def singular_jsonifier(self, obj):
        x = {}
        for attr in obj.__dict__:
            z = getattr(obj, attr)
            print(attr, ":", z)
            if attr == '_sa_instance_state': 
                continue

            if isinstance(z, datetime):
                z = datetime.strftime(z, format='%Y-%m-%d %H:%M:%S')

            if isinstance(z, float):
                z = int(z)

            if isinstance(z, WKBElement):
                z = mapping(shape.to_shape(z))
            
            x[attr] = z
        return x