from flask import Flask
import json

class RequestFactory:
    
    app: Flask = None
    
    def __init__(self, app: Flask):
        self.app = app
        
    def makeResponse(self, responseObj: object):
        response = self.app.response_class(
            response=json.dumps(responseObj),
            status=200,
            mimetype='application/json'
        )
        return response
    
    def responseSuccess(self, content: object):
        if (content == None or content == {}):
            obj = {
                "result": 0
            }
        else:
            obj = {
                "result": 0,
                "content": content
            }
        return self.makeResponse(obj)

    def responseError(self, result: int, description: str):
        obj = {
            "result": result,
            "description": description
        }
        return self.makeResponse(obj)