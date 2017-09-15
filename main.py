from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/cluster_info')
def info():
    pass

if __name__ == '__main__':
    app.run(debug=False, port=5500, host='0.0.0.0')
