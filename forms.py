from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EncryptForm(FlaskForm):
    text = StringField('Text to Encrypt', validators=[DataRequired()])
    submit = SubmitField('Encrypt')
class DecryptForm(FlaskForm):
    encrypted_text = StringField('Text to Decrypt', validators=[DataRequired()])
    submit = SubmitField('Decrypt')
