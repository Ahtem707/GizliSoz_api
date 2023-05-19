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
    
    def getLevels(self, request):
        print("myLog: getLevels 1")
        if request.method != 'GET':
            return self.reqFactory.responseError(1, "Неправильный метод запроса")
        print("myLog: getLevels 2")
        print("myLog: getLevels",request.args)
        try:
            levelsNumber = list(request.args.get('levelsNumber'))
            translateLang = str(request.args.get('translateLang'))
            voiceoverActor = str(request.args.get('voiceoverActor'))
            characterType = str(request.args.get('characterType'))
            print("myLog: getLevels 3")
        except:
            print("myLog: getLevels 4")
            return self.reqFactory.responseError(1, "Неправильные параметры или их тип")

        print("myLog: levelsNumber",levelsNumber)
        levels = []
        for index in levelsNumber:
            level = getJson(f"./sample/level_{index}.json")
            if level != None: levels.append(level)
        
        obj = {
            "levels": levels
        }
        
        return self.reqFactory.newresponseSuccess(obj)