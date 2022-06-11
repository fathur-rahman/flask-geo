from app import db
from datetime import datetime
from sqlalchemy import Column

from geoalchemy2 import Geometry


class BE_PYTHON(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    geometry = Column(Geometry(srid=4326), nullable = True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.name)