from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms.validators import data_required, ValidationError
from wtforms import StringField, SubmitField, EmailField, TelField, URLField, PasswordField
from flask_wtf.file import FileField
from app.models import User


class RegistrationForm(FlaskForm):
	name = StringField('name', validators=[data_required()])
	email = EmailField('email', validators=[data_required()])
	password = PasswordField('password', validators=[data_required()])
	submit = SubmitField('Create account')

	def validate_name(self, name):
		user = User.query.filter_by(name=name.data).first()
		if user:
			raise ValidationError('name is already taken, choose another')


	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('email is already taken, choose another')


class LoginForm(FlaskForm):
	name = StringField('name', validators=[data_required()])
	email = EmailField('email', validators=[data_required()])
	password = PasswordField('password', validators=[data_required()])
	submit = SubmitField('log in')


class AddBusiness(FlaskForm):
	name = StringField('name', validators=[data_required()])
	category = StringField('category', validators=[data_required()])
	phone = TelField('phone', validators=[data_required()])
	email = EmailField('email')
	website = URLField('website')
	facebook = URLField('facebook')
	address = StringField('address')
	sentence = StringField('about')
	logo = FileField('image')
	submit = SubmitField('Create your business card now')


class UpdateCard(FlaskForm):
	name = StringField('name', validators=[data_required()])
	category = StringField('category', validators=[data_required()])
	phone = TelField('phone', validators=[data_required()])
	email = EmailField('email')
	website = URLField('website')
	facebook = URLField('facebook')
	address = StringField('address')
	sentence = StringField('about')
	logo = FileField('image')
	submit = SubmitField('Update card')


	def validate_name(self, name):
		if name.data != current_user.name:
			user = User.query.filter_by(name=name.data).first()
			if user:
				raise ValidationError('name is already taken, choose another')


	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('email is already taken, choose another')
