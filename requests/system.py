from extensions.RequestFactory import *
from extensions.FileManager import *

class System:
    app = None
    reqFactory = None
    
    def __init__(self, app):
        self.app = app
        self.reqFactory = RequestFactory(app)
        
    def checkConnect(self, request):
        return self.reqFactory.newresponseSuccess(None)
    
    def appInit(self, request):
        if request.method!= 'GET':
            return self.reqFactory.responseError(1, "Неправильный метод запроса")
        
        translationLangs = [
            {
                'code': 'en',
                'value': 'English',
                'isDefault': True
            },
            {
                'code': 'ru',
                'value': 'Русский',
                'isDefault': False
            }
        ]
        voiceoverActors = [
            {
                'code': 'ahtemS',
                'value': 'Aхтем',
                'isDefault': True
            }
        ]
        levelsCount = len(findFiles("./sample/","level_"))
        obj = {
            "voiceoverHost": "http://82.146.49.164:3002/media/",
            "translationLangs": translationLangs,
            "voiceoverActors": voiceoverActors,
            "levelsCount": levelsCount
        }
        return self.reqFactory.newresponseSuccess(obj)