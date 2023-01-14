from extensions.RequestFactory import *
from extensions.FileManager import *

class Level:
    app = None
    reqFactory = None
    
    def __init__(self, app):
        self.app = app
        self.reqFactory = RequestFactory(app)
        
    def getLevelsCount(self, request):
        if request.method != 'GET':
            return self.reqFactory.responseError(1, "Неправильный метод запроса")
        
        levelscount = len(findFiles("./sample/","level_"))
        obj = {
            "levelscount": levelscount
        }
        return self.reqFactory.responseSuccess(obj)
        
        
    def getLevel(self, request):
        if request.method != 'GET':
            return self.reqFactory.responseError(1, "Неправильный метод запроса")
        
        try:
            index = int(request.args.get('index'))
        except:
            return self.request.responseError(1, "Неправильные параметры или их тип")
        
        obj = getJson(f"./sample/level_{index}.json")
        if obj == None:
            return self.reqFactory.responseError(1, "Отсутствует файл")
        return self.reqFactory.makeResponse(obj)
    
    def getLevels(self, request):
        if request.method != 'GET':
            return self.reqFactory.responseError(1, "Неправильный метод запроса")
        
        try:
            startIndex = int(request.args.get('startIndex'))
        except:
            startIndex = None
        try:
            endIndex = int(request.args.get('endIndex')) or None
        except:
            endIndex = None
        
        files = findFiles("./sample/","level_")
        result = []
        for file in files:
            level = getJson(file)
            if startIndex != None and endIndex != None:
                if startIndex <= int(level["level"]) and int(level["level"]) <= endIndex:
                    result.append(level)
            elif startIndex == None and endIndex != None:
                if int(level["level"]) <= endIndex:
                    result.append(level)
            elif startIndex != None and endIndex == None:
                if startIndex <= int(level["level"]):
                    result.append(level)
            else:
                result.append(level)
            
        # Sorted
        def levelKey(e): return e["level"]
        result.sort(key=levelKey)
        return self.reqFactory.responseSuccess(result)