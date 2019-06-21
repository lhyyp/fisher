from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
