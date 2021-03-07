from typing import Any

import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
messages = []
users = []

@app.route("/")
def hello():
    return "<b>Hello, World!</b>"


@app.route("/status")
def status():
    #Я добавил параметр username для того чтобы определить точное количество участников.Одинаковых имен может быть много.
    #Пользователи хранятся в list
    #Также мой сервер проверяет на отличие username при входе в чат.Если username был использован,он просит
    # ввести username заново
    #full server code: https://github.com/computerbox124/Hey-Hajiyevs/blob/master/server.py
    dt = datetime.now()
    return {
        'status': True,
        'name': 'Hajiyevs Messenger',
        'time': time.time(),
        'time1': time.asctime(),
        'time2': dt,
        'time3': str(dt),
        'time4': dt.isoformat(),
        'time5': dt.strftime('%d %b %H:%M:%S'),
        'username_count': 'At the moment there are ' + str(len(users)) + ' users online.'
    }


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)

    name = data.get('name')
    text = data.get('text')
    username = data.get('username')
    status = data.get('status')

    if not isinstance(name, str) or len(name) == 0:
        return abort(400)

    if not isinstance(username, str) or len(username) == 0:
        return abort(400)

    if not isinstance(status, str) or len(status) == 0:
        return abort(400)

    if username in users and status == 'login':
        return {'status': 'User with such username was created!'}

    if status == 'login':
        users.append(username)
        return {'status': 'Ok'}
    elif status == 'logout':
        users.remove(username)
        return {'status': 'Ok'}

    if not isinstance(text, str) or \
            len(text) == 0 or len(text) > 1000:
        return abort(400)

    message = {
        'name': name,
        'text': text,
        'time': time.time(),
        'username': username
    }
    messages.append(message)

    return {'status':'Ok'}


@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    response = []
    for message in messages:
        if message['time'] > after:
            response.append(message)

    return {'messages': response[:50]}


app.run()