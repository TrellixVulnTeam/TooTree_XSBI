from flask_wtf import FlaskForm 
from wtforms import SelectField,SubmitField
from wtforms.validators import DataRequired

class SelectBorough(FlaskForm):
    borough = SelectField('Borough', validators=[DataRequired()])
    submit = SubmitField('See Trees')