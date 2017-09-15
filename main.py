from flask import Flask
from flask_cors import CORS
import config
import grequests
from flask.json import jsonify

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/cluster_info')
def cluster_info():
    urls = config.SERVERS_LIST
    shells = (grequests.get(u) for u in urls)
    responses = grequests.map(shells)
    result = {}
    for r in responses:
        result[r.url] = {'status': r.status_code, 'text': r.text}
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=False, port=5500, host='0.0.0.0')
