from extensions.RequestFactory import *

class WordSound:
    app = None
    request = None

    mediaHost = "82.146.49.164:3002/media/"
    
    def __init__(self, app):
        self.app = app
        self.request = RequestFactory(app)

    def _getSoundUrl(self, id: int, voiceActor: str):
        if (id == 0): url = "meraba.wav"
        elif (id == 1): url = "selam.wav"
        elif (id == 2): url = "ayva.wav"
        elif (id == 3): url = "alma.wav"
        elif (id == 4): url = "armut.wav"
        elif (id == 5): url = "portaqal.wav"
        elif (id == 6): url = "qara.wav"
        elif (id == 7): url = "aq.wav"
        elif (id == 8): url = "al.wav"
        elif (id == 9): url = "sari.wav"
        elif (id == 10): url = "mavi.wav"
        elif (id == 11): url = "esil.wav"
        elif (id == 12): url = "qursaq.wav"
        elif (id == 13): url = "saqal.wav"
        elif (id == 14): url = "qulaq.wav"
        elif (id == 15): url = "tirnaq.wav"
        elif (id == 16): url = "tis.wav"
        elif (id == 17): url = "turaq.wav"
        elif (id == 18): url = "qaplan.wav"
        elif (id == 19): url = "qoy.wav"
        elif (id == 20): url = "at.wav"
        elif (id == 21): url = "qoyan.wav"
        elif (id == 22): url = "jirafe.wav"
        elif (id == 23): url = "fil.wav"
        elif (id == 24): url = "deve.wav"
        elif (id == 25): url = "narguz.wav"
        elif (id == 26): url = "lale.wav"
        elif (id == 27): url = "gul.wav"
        elif (id == 28): url = "ahudut.wav"
        elif (id == 29): url = "qavun.wav"
        elif (id == 30): url = "dut.wav"
        
        else: url = None
        return self.mediaHost + url

    def wordSound(self, request):
        if request.method != 'GET':
            return self.request.responseError(1, "Неправильный метод запроса")
        
        try:
            wordId = int(request.args.get('wordId'))
            voiceActor = str(request.args.get('voiceActor'))
        except:
            return self.request.responseError(1, "Неправильные параметры или их тип")
        
        result = self._getSoundUrl(wordId, voiceActor)
        
        if(result == None):
            return self.request.responseError(1, "На данный момент нет такого трека")
        
        obj = {
            "url": result
        }
        return self.request.responseSuccess(obj)