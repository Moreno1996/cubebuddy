from flask import Flask, request, jsonify
from flask_sqlalchemy  import SQLAlchemy
from flask_restful import Resource, Api
from os import environ

app = Flask(__name__)
api = Api(app)
times = []
names = []
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ohooefufvmascx:b797cf716109155ae89312e7508ac7de420e192ee197754698ba3a8f6b2f2068@ec2-54-225-240-168.compute-1.amazonaws.com:5432/dbp7qvupqtsftj'
db = SQLAlchemy(app)
db.create_all()
db.session.commit()


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
    def get(self,time, userName):
        from models import DailyTiming
        timeGet = DailyTiming(time, None)
        times.append(timeGet)
        db.session.add(timeGet)
        db.session.commit()
        query = DailyTiming.query.all()
        result = [q.serialize() for q in query]
        return {
            'you sent': time,
            'testQuery': result}

api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')
api.add_resource(AddNames,'/addName/<string:name>')
api.add_resource(AddTimes,'/addTime/<int:time><string:userName>')
api.add_resource(GetTimes,'/getTime/<int:time>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=environ.get("PORT", 5000),debug=False)
    #app.run(debug=True)