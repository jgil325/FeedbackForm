from flask_wtf import FlaskForm
try:
    from wtforms import TextAreaField, SubmitField, Form, fields
    from wtforms.fields.html5 import IntegerField
    from wtforms.fields import html5 as h5fields
    from wtforms.widgets import html5 as h5widgets
    from wtforms.validators import DataRequired, Optional
except ImportError:
    print("Import Error")


class SurveyForm(FlaskForm):
    rating = IntegerField('Choose a rating:', widget=h5widgets.NumberInput(min=0, max=5, step=1), validators=[DataRequired()])
    text_area = TextAreaField('comments')    
    submit = SubmitField('Submit')
