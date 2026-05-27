import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

@app.route('/debug')
def debug():
    return jsonify({
        'base': BASE,
        'files': os.listdir(BASE)
    })

@app.route('/')
def home():
    return send_from_directory(BASE, 'index.html')

@app.route('/<path:filename>')
def files(filename):
    return send_from_directory(BASE, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
