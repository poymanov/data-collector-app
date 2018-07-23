from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email


class DataForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	height = DecimalField('Height', validators=[DataRequired()])
	submit = SubmitField('Submit')