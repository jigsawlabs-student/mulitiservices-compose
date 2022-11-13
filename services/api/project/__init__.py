from flask import Flask, jsonify
from postgres import Postgres
import os

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
connection = Postgres(SQLALCHEMY_DATABASE_URI)

connection.run("CREATE TABLE users (name text)")
connection.run("INSERT INTO users VALUES ('maggie simpson')")

@app.route('/users')
def index():
    users = connection.all('SELECT * FROM users;')
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(debug=True)
