from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/send-data', methods=['POST'])
def receive_data():
    data = request.json.get('data')
    with open('data.txt', 'a') as f:
        f.write(data + '\n')
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
