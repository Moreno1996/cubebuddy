from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from os import environ

app = Flask(__name__)
api = Api(app)
app.run(environ.get('PORT'))

names = []
class HelloWorld(Resource):
    def get(self):
        return{'about':'Hellow Worlds'}
    def post(self):
        some_json = request.get_json()
        return {'you sent' : some_json},201

class Multi(Resource):
    def get(self,num):
        return {'result': num*10}
class addNames(Resource):
    def get(self,name):
        names.append(name)
        return {
            'you sent': name,
            'all Names': names}
api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')
api.add_resource(addNames,'/addName/<string:name>')

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)