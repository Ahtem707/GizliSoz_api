from extensions.RequestFactory import *

class System:
    app = None
    request = None
    
    def __init__(self, app):
        self.app = app
        self.request = RequestFactory(app)
        
    def checkConnect(self, request):
        return self.request.responseSuccess(None)