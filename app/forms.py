from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Email


class DataForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	height = FloatField('Height', validators=[DataRequired()])
	submit = SubmitField('Submit')