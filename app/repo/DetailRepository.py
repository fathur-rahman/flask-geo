from app.jsonifier import Jsonifier
from app.repo.Repository import Repository
from app.models.models import BE_PYTHON, detail


class DetailRepository(Repository):
    __instance = None
    model = detail

    def __new__(cls):
        if DetailRepository.__instance is None:
            DetailRepository.__instance = object.__new__(cls)

        return DetailRepository.__instance

    def getAll(self):        
        return Jsonifier().jsonifier(detail.query.all())
