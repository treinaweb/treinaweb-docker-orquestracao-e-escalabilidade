from flask import render_template, redirect, url_for
from app import app
from app.forms import FormCadastrarVotacao

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/construcao")
def construcao():
    return render_template("construcao.html")

@app.route("/votacoes")
def votacoes():
    return render_template("votacoes.html")

@app.route("/cadastrar_votacao", methods=['GET','POST'])
def cadastrar_votacao():
    form=FormCadastrarVotacao()
    if form.validate_on_submit():
        votacao = votacao(votacao=form.votacao.data)
        return votacao
    return render_template("cadastrar_votacao.html", title="Cadastrar Votacao", form=form)