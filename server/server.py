from time import time

from flask import Flask, request
from hashlib import sha1
from sqlite3 import connect

app = Flask(__name__)

connection = connect("server/messages")
cursor = connection.cursor()
cursor.execute('DELETE FROM messages;')
connection.commit()
cursor.close()
connection.close()


@app.route("/")
def home_page():
    return "SPU server's home page"


@app.route("/load_messages")
def load_messages():
    previous_send = float(request.args["previous_send"])
    result = list()
    connection = connect("server/messages")
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM messages;')
    data = cursor.fetchall()
    for info in data:
        if info[3] > previous_send:
            result.append(info)

    cursor.close()
    connection.close()
    return {"messages": result}


@app.route("/upload_message", methods=["POST"])
def upload_message():
    username = request.json["username"]
    message = request.json["message"]
    connection = connect("server/messages")
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO messages (username, message, time) VALUES ("{username}", "{message}", "{time()}");')
    connection.commit()
    print(f'{username}: {message}')

    cursor.close()
    connection.close()
    return [0]


@app.route("/authorization")
def authorization():
    username = request.args["username"]
    password = request.args["password"]
    connection = connect('server/users')
    cursor = connection.cursor()
    success = False

    cursor.execute(f'SELECT * FROM users WHERE username="{username}";')
    value = cursor.fetchall()

    hashed_password = sha1(password.encode()).hexdigest()

    if value != [] and value[0][2] == hashed_password:
        print(f'Success authorization by {username}')
        success = True
    else:
        print(f'Incorrect username {username} or password')

    cursor.close()
    connection.close()
    return [success]


@app.route("/registration", methods=["POST"])
def registration():
    username = request.json["username"]
    password = request.json["password"]
    connection = connect('server/users')
    cursor = connection.cursor()
    success = False

    cursor.execute(f'SELECT * FROM users WHERE username="{username}";')
    value = cursor.fetchall()

    if not value:
        hashed_password = sha1(password.encode()).hexdigest()
        cursor.execute(f'INSERT INTO users (username, password) VALUES ("{username}", "{hashed_password}");')
        connection.commit()
        print(f'Successfully registration by {username}')
        success = True
    else:
        print(f'User with name {username} already exists')

    cursor.close()
    connection.close()
    return [success]


@app.route("/deletion", methods=["POST"])
def deletion():
    username = request.json["username"]
    connection = connect('server/users')
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM users WHERE username="{username}";')
    connection.commit()

    cursor.close()
    connection.close()
    print(f"Deleted {username}'s account")
    return [1]


def launch_server():
    app.run()
