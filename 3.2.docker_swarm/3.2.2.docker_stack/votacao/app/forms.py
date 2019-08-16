from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class VoteForm(FlaskForm):
    vote = StringField('Vote', 
                        validators=[DataRequired()])

class FormCadastrarVotacao(FlaskForm):
    votacao = StringField('Nome da Votação:',
                          validators=[DataRequired])
    cadastrar = SubmitField('Cadastrar Votação')