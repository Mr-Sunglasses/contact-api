from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class Query_User(FlaskForm):
    name = StringField(label="Name: ", validators=[DataRequired()])
    email = EmailField(label="Email: ", validators=[DataRequired(), Email()])
    message = TextAreaField(label="Your Query", validators=[DataRequired()])
    submit = SubmitField(label="Submit")