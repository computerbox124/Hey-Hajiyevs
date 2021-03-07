import requests

# response = requests.get(
#     'http://127.0.0.1:5000/status'
# )
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.json()['name'])
sig = 0
name = input('Input your name: ')
while True:
    if sig == 0:
        username = input('Input your username: ')
        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={'name': name, 'username': username, 'text': '','status': 'login'}
        )
        data = response.json()
        if data['status'] == 'Ok':
            break
        else:
            sig = 1

    else:
        username = input('That username was used: Input your username again: ')
        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={'name': name, 'username': username, 'text': '', 'status': 'login'}
        )
        data = response.json()
        if data['status'] == 'Ok':
            break



while True:
    text = input('Input your text:')
    if text == "/logout":
        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={'name': name, 'username': username, 'text': text, 'status': 'logout'}
        )
        exit()
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'name': name, 'username': username, 'text': text, 'status': 'chat'}
    )
