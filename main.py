from flask import Flask
from flask_cors import CORS
import config
from flask.json import jsonify
from data_fetcher import DataFetcher

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/cluster_info')
def cluster_info():
    clusters = config.CLUSTERS_LIST
    result = {}
    for k in clusters:
        data_fetcher = DataFetcher(clusters[k])
        result[k] = data_fetcher.get_info()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, port=5500, host='0.0.0.0')
