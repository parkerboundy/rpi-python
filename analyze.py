import sqlite3

from flask import Flask
from flask import render_template
from flask import g

app = Flask(__name__, template_folder='analyze/templates', static_folder='analyze/static')


def connect_db():
	return sqlite3.connect('db/box.db')

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.template_filter('countattribute')
def countattribute(list, attribute, value):
	return sum(x[attribute] == value for x in list)

@app.before_request
def before_request():
    g.db = connect_db()
    g.db.row_factory = sqlite3.Row

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
	races = query_db("SELECT * FROM races ORDER BY id ASC")
	return render_template('home.html', races=races)

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/races/<int:race_id>')
def show_race(race_id):
	race = query_db("SELECT * FROM races WHERE id = ?", [race_id], one=True)
	return render_template('race.html', race=race)

@app.route('/stats')
def stats():
	return render_template('stats.html')

if __name__ == '__main__':
	app.run(debug=True)