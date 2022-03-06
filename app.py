import os, json

import requests
from flask import Flask, jsonify, request, make_response, abort
from functions import *
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['GET', 'POST'])
def perform_query():
    if request.method == "POST":
        payload = request.json
        file_name = payload.get('file_name')
        if file_name:
            path = f'{DATA_DIR}\\{file_name}'
            if os.path.exists(path):
                cmd1 = payload.get('cmd1')
                value1 = payload.get('value1')
                cmd2 = payload.get('cmd2')
                value2 = payload.get('value2')
                result = []
                if cmd1:
                    if cmd1 == 'filter':
                        result = filter_file(readfile(path), word=value1)
                    elif cmd1 == 'sort':
                        result = sort_file(readfile(path), reverse=value1)
                    elif cmd1 == 'map':
                        result = map_file(readfile(path), row=int(value1))
                    elif cmd1 == 'limit':
                        result = limit_data(readfile(path), limit=int(value1))
                    elif cmd1 == 'unique':
                        result = unique_(readfile(path))
                if cmd2:
                    if cmd2 == 'filter':
                        result = filter_file(result, word=value2)
                    elif cmd2 == 'sort':
                        result = sort_file(result, reverse=value2)
                    elif cmd2 == 'limit':
                        result = limit_data(result, limit=int(value2))
                    elif cmd2 == 'map':
                        result = map_file(result, row=int(value2))
                    elif cmd2 == 'unique':
                        result = unique_(result)
                return json.dumps(result)
            else:
                abort(404)

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
    # payload = {
    #     'file_name': 'apache_logs.txt',
    #     'cmd1': 'map',
    #     'value1': '0',
    #     'cmd2': 'limit',
    #     'value2': '3'
    # }
    # client = app.test_client()
    # response = client.post('/perform_query', json=payload)
    # print(response.data)