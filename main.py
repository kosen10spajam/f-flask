from __future__ import print_function, unicode_literals

import sqlite3
from flask import Flask, request as req, jsonify
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)
_sql = sqlite3.connect('database.db', check_same_thread=False)
sql = _sql.cursor()

@app.route('/')
def index():
    return jsonify({'msg': 'Hello Sonoba!'})

@app.route('/admin')
def admin():
    return app.send_static_file('admin.html')


if __name__ == '__main__':
    sql.execute('DROP TABLE IF EXISTS players')
    sql.execute('CREATE TABLE players (pid integer primary key, name text)')
    app.run()
