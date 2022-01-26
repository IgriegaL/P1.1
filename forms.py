from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length



class SignupForm(FlaskForm): #la clase SignupForm hereda de FlaskForm
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título slug', validators=[Length(max=128)])
    content = StringField('Contenido')
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')

#El campo remember_me es de tipo BooleanField. Deberás importarlo junto al resto de tipos que importamos en la lección anterior. Lo utilizaremos para dar la posibilidad al usuario de mantener la sesión incluso después de cerrar el navegador.