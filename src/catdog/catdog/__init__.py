
# ok
# we don't stop running, now

# how to separate flask app into multiple files
# list of bits of the app
# html tabs for all the bits of the app
# mysoc lookup

# actions:
# display recipients
# tab scaffolding
# preview
# dispatch

import sqlite3

from flask import Flask


from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///mk_blog'
db = SQLAlchemy(app)

import routes

def start():
    app.run(debug=True)

if __name__ == '__main__':
    start()
