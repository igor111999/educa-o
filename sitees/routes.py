# criar os links do nosso site
from flask import render_template, url_for, redirect
from sitees import app, database, bcrypt
from sitees.models import Usuario, Fotos
from flask_login import login_required, login_user, logout_user, current_user
from sitees.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename
from sitees.static import conteudos

@app.route("/matematica", methods=["GET", "POST"])
def matematica():
    return render_template('contmat.html')

@app.route("/fis", methods=["GET", "POST"])
def fis():
    return render_template('contfisica.html')

@app.route("/jog", methods=["GET", "POST"])
def jog():
    return render_template('jogos.html')

@app.route("/igor", methods=["GET", "POST"])
def igor():
    return render_template('igor.html')

@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template('ICG.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for("ICG", id_usuario=usuario.id))
    return render_template('homepage.html', form=formlogin)


@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data,
                          email=formcriarconta.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("ICG", id_usuario=usuario.id))
    return render_template('criar_conta.html', form=formcriarconta)

@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        # se o usuario estiver vendo proprio perfil
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # salvar o arqivo na pasta post
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)
            # registrar o arquivo no banco de dados
            foto = Fotos(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template('perfil.html', usuario=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed():
    fotos = Fotos.query.order_by(Fotos.data_criacao.desc()).all()
    return render_template("feed.html", fotos=fotos)

@app.route("/algebra", methods=["GET", "POST"])
def algebra():
    return render_template('algebra.html')

@app.route("/ana", methods=["GET", "POST"])
def ana():
    return render_template('analise.html')

@app.route("/ang", methods=["GET", "POST"])
def ang():
    return render_template('Angulos.html')

@app.route("/ante", methods=["GET", "POST"])
def ante():
    return render_template('antesucessor.html')

@app.route("/base", methods=["GET", "POST"])
def base():
    return render_template('basedez.html')

@app.route("/jun", methods=["GET", "POST"])
def jun():
    return render_template('conjnum.html')

@app.route("/geom", methods=["GET", "POST"])
def geom():
    return render_template('definicaogeo.html')

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    return render_template('distanciapontos.html')

@app.route("/diz", methods=["GET", "POST"])
def diz():
    return render_template('dizimap.html')

@app.route("/equ", methods=["GET", "POST"])
def equ():
    return render_template('equacoes.html')

@app.route("/expr", methods=["GET", "POST"])
def expr():
    return render_template('expressãonum.html')

@app.route("/frac", methods=["GET", "POST"])
def frac():
    return render_template('fracoes.html')

@app.route("/matr", methods=["GET", "POST"])
def matr():
    return render_template('matrizes.html')

@app.route("/med", methods=["GET", "POST"])
def med():
    return render_template('medidas.html')

@app.route("/mmc", methods=["GET", "POST"])
def mmc():
    return render_template('mmcmdc.html')

@app.route("/nota", methods=["GET", "POST"])
def nota():
    return render_template('notaçãoc.html')

@app.route("/nun", methods=["GET", "POST"])
def nun():
    return render_template('numerosnat.html')

@app.route("/prop", methods=["GET", "POST"])
def prop():
    return render_template('proporcao.html')


@app.route("/quat", methods=["GET", "POST"])
def quat():
    return render_template('quatroop.html')


@app.route("/reg", methods=["GET", "POST"])
def reg():
    return render_template('regrade3.html')


@app.route("/sequ", methods=["GET", "POST"])
def sequ():
    return render_template('Sequencianum.html')

