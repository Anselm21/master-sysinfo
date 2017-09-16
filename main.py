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
    clusters = config.CLUSTERS_LIST
    result = {}
    for k in clusters:
        result[k] = {}
        shells = (grequests.get(server) for server in clusters[k])
        responses = grequests.map(shells)
        for r in responses:
            result[k][r.url] = {'status': r.status_code, 'text': r.text}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, port=5500, host='0.0.0.0')
