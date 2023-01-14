from extensions.RequestFactory import *
from extensions.FileManager import *

class Crosswords:
    app = None
    reqFactory = None
    
    def __init__(self, app):
        self.app = app
        self.reqFactory = RequestFactory(app)
        
    def crosswords(self, request):
        if request.method != 'GET':
            return self.reqFactory.responseError(1, "Неправильный метод запроса")
        
        obj = getJson("./sample/levels.json")
        if obj == None:
            return self.reqFactory.responseError(1, "Отсутствует файл")
        return self.reqFactory.makeResponse(obj)