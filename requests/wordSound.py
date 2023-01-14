from extensions.RequestFactory import *

class WordSound:
    app = None
    request = None
    
    def __init__(self, app):
        self.app = app
        self.request = RequestFactory(app)

    def _getSoundUrl(self, id: int, voiceActor: str):
        if (id == 0): url = "https://www.ahtem.ru:3002/media/meraba.wav"
        elif (id == 1): url = "https://www.ahtem.ru:3002/media/selam.wav"
        elif (id == 2): url = "https://www.ahtem.ru:3002/media/ayva.wav"
        elif (id == 3): url = "https://www.ahtem.ru:3002/media/alma.wav"
        elif (id == 4): url = "https://www.ahtem.ru:3002/media/armut.wav"
        elif (id == 5): url = "https://www.ahtem.ru:3002/media/portaqal.wav"
        elif (id == 6): url = "https://www.ahtem.ru:3002/media/qara.wav"
        elif (id == 7): url = "https://www.ahtem.ru:3002/media/aq.wav"
        elif (id == 8): url = "https://www.ahtem.ru:3002/media/al.wav"
        elif (id == 9): url = "https://www.ahtem.ru:3002/media/sari.wav"
        elif (id == 10): url = "https://www.ahtem.ru:3002/media/mavi.wav"
        elif (id == 11): url = "https://www.ahtem.ru:3002/media/esil.wav"
        elif (id == 12): url = "https://www.ahtem.ru:3002/media/qursaq.wav"
        elif (id == 13): url = "https://www.ahtem.ru:3002/media/saqal.wav"
        elif (id == 14): url = "https://www.ahtem.ru:3002/media/qulaq.wav"
        elif (id == 15): url = "https://www.ahtem.ru:3002/media/tirnaq.wav"
        elif (id == 16): url = "https://www.ahtem.ru:3002/media/tis.wav"
        elif (id == 17): url = "https://www.ahtem.ru:3002/media/turaq.wav"
        elif (id == 18): url = "https://www.ahtem.ru:3002/media/qaplan.wav"
        elif (id == 19): url = "https://www.ahtem.ru:3002/media/qoy.wav"
        elif (id == 20): url = "https://www.ahtem.ru:3002/media/at.wav"
        elif (id == 21): url = "https://www.ahtem.ru:3002/media/qoyan.wav"
        elif (id == 22): url = "https://www.ahtem.ru:3002/media/jirafe.wav"
        elif (id == 23): url = "https://www.ahtem.ru:3002/media/fil.wav"
        elif (id == 24): url = "https://www.ahtem.ru:3002/media/deve.wav"
        elif (id == 25): url = "https://www.ahtem.ru:3002/media/narguz.wav"
        elif (id == 26): url = "https://www.ahtem.ru:3002/media/lale.wav"
        elif (id == 27): url = "https://www.ahtem.ru:3002/media/gul.wav"
        elif (id == 28): url = "https://www.ahtem.ru:3002/media/ahudut.wav"
        elif (id == 29): url = "https://www.ahtem.ru:3002/media/qavun.wav"
        elif (id == 30): url = "https://www.ahtem.ru:3002/media/dut.wav"
        
        else: url = None
        return url

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