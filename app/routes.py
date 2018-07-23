from app import app
from flask import render_template, request
from app.forms import DataForm

@app.route('/')
def home():
	form = DataForm()
	return render_template('home.html', form=form)

@app.route('/success', methods=['POST'])
def success():
	email = request.form['email']
	height = request.form['height']
	return render_template('success.html')	