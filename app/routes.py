from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import DataForm
from app.models import Data

@app.route('/')
def home():	
	form = DataForm()
	return render_template('home.html', form=form)

@app.route('/success', methods=['POST'])
def success():
	form = DataForm()
	if form.validate_on_submit():
		if Data.query.filter_by(email=form.email.data).first():			
			flash('Validation errors')
			form.email.errors.append('Email address already exists.')
			return render_template('home.html', form=form)

		data = Data(email=form.email.data, height=form.height.data)
		db.session.add(data)
		db.session.commit()

		return render_template('success.html')	
	else:
		flash('Validation errors')
		return render_template('home.html', form=form)
	