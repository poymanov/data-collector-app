from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/success', methods=['POST'])
def success():
	email = request.form['email']
	height = request.form['height']
	return render_template('success.html')	