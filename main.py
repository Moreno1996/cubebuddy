from flask import Flask, request, jsonify
from flask_sqlalchemy  import SQLAlchemy
from flask_restful import Resource, Api
from os import environ

app = Flask(__name__)
api = Api(app)
times = []
names = []
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://uwemzddveqrlwh:b5f6f2a85176583be8fa5d13738ed2f9f0d35c15057c974cd518d4e54c224aa1@ec2-54-247-89-189.eu-west-1.compute.amazonaws.com:5432/d6c6au1ssndtng'
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

class AddTimes(Resource):
    def get(self,time):
        from models import DailyTiming
        timeGet = DailyTiming(time, None)
        times.append(timeGet)
        db.session.add(timeGet)
        db.session.commit()
        query = DailyTiming.query.all()
        result = [q.serialize() for q in query]
        return {
            'you sent': time,
            'testQuery' : result}

api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')
api.add_resource(AddNames,'/addName/<string:name>')
api.add_resource(AddTimes,'/addTime/<int:time>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=environ.get("PORT", 5000),debug=False)
    #app.run(debug=True)