from flask_wtf import FlaskForm
try:
    from wtforms import StringField, SubmitField, Form, fields
    from wtforms.validators import DataRequired, Length, Email, EqualTo
except ImportError:
    print("Import Error")


class SurveyForm(FlaskForm):
    rating = fields.RadioField('What would you rate this experience?',
            choices=[('1','1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    comments = fields.TextAreaField('If you have any additional feedback about passwords or this survey, please enter your comments here.', default=None)
    submit = SubmitField('Submit')
