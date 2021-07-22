from flask_wtf import FlaskForm
try:
    from wtforms import StringField, PasswordField, SubmitField, BooleanField
    from wtforms.validators import DataRequired, Length, Email, EqualTo
except ImportError:
    print("Import Error")


class SurveyForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    rating = SelectField(
        u'Rating', choices=[
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[
            DataRequired()])
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')
