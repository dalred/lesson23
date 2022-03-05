import os, json

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['GET'])
def perform_query():
    # if request.method == "POST":
    #     query = request.args.get('query')
    #     file_name = request.args.get('file_name')
    #     if os.path.exists(DATA_DIR//file_name):

    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    #return app.response_class('[1, 2, 3]', content_type="text/plain")
    return json.dumps([1, 2, 3])

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
