from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='analyze/templates', static_folder='analyze/static')

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/races/<int:race_id>')
def show_race(race_id):
	return render_template('race.html')

@app.route('/stats')
def stats():
	return render_template('stats.html')

if __name__ == '__main__':
	app.run(debug=True)