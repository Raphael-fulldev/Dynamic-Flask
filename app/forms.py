from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList, FormField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import Subscription

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')
#
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=0, max=64)]) #max 64 so it doesn't exceed database allocated field (models.py)
#     email = StringField('Email', validators=[DataRequired(), Email(), Length(min=0, max=120)])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')
#
#     # wtforms method to define custom validator for the Registration Form
#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first() #username field in the form
#         if user is not None:
#             raise ValidationError('Username already exists. Please try a different one.')
#
#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first() #can search because there is index on this db field as well (inside models.py)
#         if user is not None:
#             raise ValidationError('Email already exists.')

class SubscriptionForm(FlaskForm):
    company = StringField(('Company'), validators=[DataRequired(), Length(min=0, max=20)])
    description = StringField(('Description'), validators=[Length(min=0, max=120)])
    # price = StringField(('Price'), validators=[DataRequired(), Length(min=0, max=6)])
    # next_payment_date = StringField(('Next Payment Date'), validators=[DataRequired()])
    # payment_frequency = StringField(('Payment Frequency'), validators=[DataRequired(), Length(min=0, max=4)])
    # category = StringField(('Category'), validators=[Length(min=0, max=50)])
    save = SubmitField('Save')


    def __repr__(self):
        return f'<Subscription {self.company}>'

    @staticmethod
    def convert_payment_frequency_to_days(payment_frequency):
        if payment_frequency == 'weekly':
            payment_frequency = 7

class MainSubscriptionForm(FlaskForm):
    subscription = FieldList(FormField(SubscriptionForm), min_entries=1)