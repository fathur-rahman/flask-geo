from app.jsonifier import jsonifier
from app.repo.Repository import Repository
from app.models.models import BE_PYTHON


class DataRepository(Repository):
    __instance = None
    model = BE_PYTHON

    def __new__(cls):
        if DataRepository.__instance is None:
            DataRepository.__instance = object.__new__(cls)

        return DataRepository.__instance

    def getAll(self):        
        return jsonifier().jsonifier(BE_PYTHON.query.all())
