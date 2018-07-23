from app import app
from flask import render_template, request

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/success', methods=['POST'])
def success():
	email = request.form['email']
	height = request.form['height']
	return render_template('success.html')	