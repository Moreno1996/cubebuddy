from flask import Flask, request,jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

names = []

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}),201
    else:
        return jsonify({"about":"Hello World!"})

@app.route('/multi/<int:num>',methods=['GET'])
def get_multiply10(num):
    return jsonify({'result':num*10})

@app.route('/addName/<string:name>', methods=['GET'])
def addName(name):
    names.append(name)
    return jsonify({
        'you sent':name,
        'all Names': names})



if __name__ == '__main__':
    app.run(debug=True)