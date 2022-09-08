import os
from utils import query_constructor
from flask import Flask, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/")
def starter_page():
    return f"Привет! Это стартовая страница, попробуйте запрос: /perform_query/?cmd1=filter&value1=POST"


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    try:
        cmd_1 = request.args.get('cmd_1')
        value_1 = request.args.get('value_1')
        cmd_2 = request.args.get('cmd_2')
        value_2 = request.args.get('value_2')
        file_name = request.args.get('file_name')

        if not (cmd_1 and value_1 and file_name):
            return {"Error 400 - Bad Request. Какой-то из параметров или файл отсутсвует"}, 400

    except:
        return {"Error 400 - Bad Request. Отсутствуеют необходимые параметры"}, 400

    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return {"Error 400 - Bad Request. Файл не найден"}, 400

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            result_first = query_constructor(cmd_1, value_1, file)
            result_second = query_constructor(cmd_2, value_2, result_first)
            result_final = "\n".join(result_second)

    except:
        return {"Error - Не удалось прочитать файл"}

    # вернуть пользователю сформированный результат
    return app.response_class(result_final, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
