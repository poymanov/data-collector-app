from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import DataForm
from app.models import Data
from app.email import send_email
from sqlalchemy.sql import func

@app.route('/')
def home():		
	form = DataForm()
	return render_template('home.html', form=form)

@app.route('/success', methods=['POST'])
def success():
	form = DataForm()
	email = form.email.data
	height = form.height.data

	if form.validate_on_submit():
		if Data.query.filter_by(email=email).first():			
			flash('Validation errors')
			form.email.errors.append('Email address already exists.')
			return render_template('home.html', form=form)

		data = Data(email=email, height=height)
		db.session.add(data)
		db.session.commit()
		
		average_height = db.session.query(func.avg(Data.height)).scalar()
		average_height = round(average_height, 1)
		people_count = db.session.query(Data).count()

		text_body = render_template('/email/height_mail.txt', height=height, average_height=average_height, people_count=people_count)
		html_body = render_template('/email/height_mail.html', height=height, average_height=average_height, people_count=people_count)
		send_email(subject="Height data", recipients=[email], text_body=text_body, html_body=html_body)

		return render_template('success.html')	
	else:
		flash('Validation errors')
		return render_template('home.html', form=form)
	