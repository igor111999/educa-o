# criar os links do nosso site
from flask import render_template, url_for, redirect
from sitees import app, database, bcrypt
from sitees.models import Usuario, Fotos
from flask_login import login_required, login_user, logout_user, current_user
from sitees.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename
from sitees.static import conteudos

@app.route("/cine", methods=["GET", "POST"])
def cine():
    return render_template('templates_fis/cinem.html')

@app.route("/noti", methods=["GET", "POST"])
def noti():
    return render_template('templates_fis/notaçãoc.html')

@app.route("/quda", methods=["GET", "POST"])
def quda():
    return render_template('templates_fis/quedali.html')

@app.route("/reti", methods=["GET", "POST"])
def reti():
    return render_template('templates_fis/retivetees.html')

@app.route("/siste", methods=["GET", "POST"])
def siste():
    return render_template('templates_fis/sistemad.html')

@app.route("/cula", methods=["GET", "POST"])
def cula():
    return render_template('templates_fis/circularuni.html')

@app.route("/atri", methods=["GET", "POST"])
def atri():
    return render_template('templates_fis/forcaatrito.html')

@app.route("/deve", methods=["GET", "POST"])
def deve():
    return render_template('templates_fis/grandevetor.html')

@app.route("/gravi", methods=["GET", "POST"])
def gravi():
    return render_template('templates_fis/gravitacao.html')

@app.route("/lekp", methods=["GET", "POST"])
def lekp():
    return render_template('templates_fis/leisdekepler.html')

@app.route("/lenw", methods=["GET", "POST"])
def lenw():
    return render_template('/templates_fis/leisdenewton.html')

@app.route("/qdre", methods=["GET", "POST"])
def qdre():
    return render_template('templates_fis/quedaresisten.html')

@app.route("/unfm", methods=["GET", "POST"])
def unfm():
    return render_template('templates_fis/unidaforcmass.html')

@app.route("/vdac", methods=["GET", "POST"])
def vdac():
    return render_template('templates_fis/variaçõesdaaceleracao.html')

@app.route("/alcm", methods=["GET", "POST"])
def alcm():
    return render_template('templates_fis/altercampmagn.html')

@app.route("/cmm", methods=["GET", "POST"])
def cmm():
    return render_template('templates_fis/cammagneti.html')

@app.route("/cpunt", methods=["GET", "POST"])
def cpunt():
    return render_template('templates_fis/campelepuntu.html')

@app.route("/gascp", methods=["GET", "POST"])
def gascp():
    return render_template('templates_fis/comporgases.html')

@app.route("/ctel", methods=["GET", "POST"])
def ctel():
    return render_template('templates_fis/corretele.html')

@app.route("/disl", methods=["GET", "POST"])
def disl():
    return render_template('templates_fis/dilacaosoliq.html')

@app.route("/eleti", methods=["GET", "POST"])
def eleti():
    return render_template('templates_fis/eletrizacao.html')

@app.route("/fasesgl", methods=["GET", "POST"])
def fasesgl():
    return render_template('templates_fis/fasesgasliqsol.html')

@app.route("/fele", methods=["GET", "POST"])
def fele():
    return render_template('templates_fis/forcelemotr.html')

@app.route("/inde", methods=["GET", "POST"])
def inde():
    return render_template('templates_fis/induceletreonda.html')

@app.route("/lecl", methods=["GET", "POST"])
def lecl():
    return render_template('templates_fis/leidecoul.html')

@app.route("/letd", methods=["GET", "POST"])
def letd():
    return render_template('/templates_fis/leisdatermodi.html')

@app.route("/lifr", methods=["GET", "POST"])
def lifr():
    return render_template('templates_fis/linhdfor.html')

@app.route("/mond", methods=["GET", "POST"])
def mond():
    return render_template('templates_fis/movimond.html')

@app.route("/ohm", methods=["GET", "POST"])
def ohm():
    return render_template('templates_fis/ohmeresis.html')

@app.route("/feipl", methods=["GET", "POST"])
def feipl():
    return render_template('templates_fis/ondsonefeidople.html')

@app.route("/qdres", methods=["GET", "POST"])
def qdres():
    return render_template('templates_fis/quedaresisten.html')

@app.route("/refl", methods=["GET", "POST"])
def refl():
    return render_template('templates_fis/reflexaluz.html')

@app.route("/refr", methods=["GET", "POST"])
def refr():
    return render_template('templates_fis/refracaluz.html')

@app.route("/tempee", methods=["GET", "POST"])
def tempee():
    return render_template('templates_fis/TempEscalas.html')

@app.route("/unfms", methods=["GET", "POST"])
def unfms():
    return render_template('templates_fis/unidadorcmass.html')

@app.route("/vapre", methods=["GET", "POST"])
def vapre():
    return render_template('templates_fis/vaporepress.html')

@app.route("/tdm", methods=["GET", "POST"])
def tdm():
    return render_template('/templates_fis/termodin.html')
