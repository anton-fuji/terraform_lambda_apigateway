from flask import  Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': "Hello, lambda!"})

@app.route('/testing', methods=['GET'])
def testing():
    return jsonify({'message': "testing, lambda!!"})

if __name__ == '__main__':
    app.run(debug=True)
