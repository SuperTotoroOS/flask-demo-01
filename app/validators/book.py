"""
Created by Ricky Yang on 24/10/19
@File: book.py
@Description:
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    query = StringField(validators=[
        DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[
        NumberRange(min=1, max=99)], default=1)
