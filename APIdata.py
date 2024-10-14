import csv
import os 
from flask import Flask, jsonify, send_file
from 314 import get

app = Flask(__name__)
data = get()

@app.route('/เดต้าตามสไตล', methods=['GET'])
def get_csv_data():
    json_data = data.to_json(orient='records')
    return jsonify(json_data)

#192.168.1.155
#app.run(host='0.0.0.0', port=5000)