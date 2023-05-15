from extensions.RequestFactory import *
from extensions.FileManager import *

class Level:
    app = None
    request = None
    reqFactory = None
    
    def __init__(self, app):
        self.app = app
        self.reqFactory = RequestFactory(app)
    
    def getLevel(self, request):
        if request.method != 'GET':
            return self.reqFactory.responseError(1, "Неправильный метод запроса")
        
        try:
            index = int(request.args.get('levelNumber'))
            translateLang = str(request.args.get('translateLang'))
            voiceoverActor = str(request.args.get('voiceoverActor'))
            characterType = str(request.args.get('characterType'))
        except:
            return self.reqFactory.responseError(1, "Неправильные параметры или их тип")
        
        obj = getJson(f"./sample/level_{index}.json")
        if obj == None:
            return self.reqFactory.responseError(1, "Отсутствует файл")
        return self.reqFactory.newresponseSuccess(obj)