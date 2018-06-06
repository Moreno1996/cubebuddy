from flask import Flask, request
from flask_sqlalchemy  import SQLAlchemy
from flask_restful import Resource, Api
from os import environ

app = Flask(__name__)
api = Api(app)
names = []
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)


class HelloWorld(Resource):

    def get(self):
        return{'about':'Hellow Worlds'}

    def post(self):
        some_json = request.get_json()
        return {'you sent' : some_json},201


class Multi(Resource):

    def get(self,num):
        return {'result': num*10}


class AddNames(Resource):

    def get(self,name):
        names.append(name)
        return {
            'you sent': name,
            'all Names': names}


api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')
api.add_resource(AddNames,'/addName/<string:name>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get("PORT", 5000),debug=False)