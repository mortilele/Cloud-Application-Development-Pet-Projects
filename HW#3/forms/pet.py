from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PetForm(FlaskForm):
    name = StringField('Pet name')
    category = StringField('Category', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = TextAreaField('Description')
    image = FileField('Image')
    submit = SubmitField('Submit')
