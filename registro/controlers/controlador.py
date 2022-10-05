from registro import app
from flask import render_template, redirect, request, session, flash
from registro.modelo.usuario import Usuario
from flask_bcrypt import Bcrypt


@app.route('/')
def principal():
    return render_template('reg.html')


@app.route('/salir')
def salir():
    session.clear()
    return redirect('/')


@app.route('/', methods=['POST'])
def crear_usuario():
    if not Usuario.validar_registro(request.form):
        return redirect('/')
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    Usuario.create(data)
    return redirect('/')


@app.route('/login', methods=['POST'])
def inicio_sesion():
    usuario = Usuario.usuario_email(request.form['email'])
    if len(usuario) == 0:
        flash('Usuario o password invalido', 'log')
        return redirect('/')
    bcrypt = Bcrypt(app)
    if bcrypt.check_password_hash(usuario[0].password, request.form['password']):
        session['usuario'] = usuario[0].__dict__
        return render_template('exito.html', usuario=usuario[0])
    else:
        flash('Usuario o password invalido', 'log')
        return redirect('/')


@app.route('/logout')
def ir():
    session.clear()
    return redirect('/')
