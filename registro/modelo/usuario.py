from registro.configuracion.mysqlconnection import BaseDeDatos
from flask_bcrypt import Bcrypt
from flask import Flask, flash
from registro import app
import re  # el módulo regex
# crea un objeto de expresión regular que usaremos más adelante
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SOLO_LETRAS_REGEX = re.compile(r'^[a-zA-Z]')


class Usuario:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']
        self.password = data['password']

    @classmethod
    def create(cls, data):
        bcrypt = Bcrypt(app)
        data['password'] = bcrypt.generate_password_hash(data['password'])
        print('data ', data)
        query = 'INSERT INTO usuario(nombre,apellido,email,password) VALUES(%(nombre)s,%(apellido)s,%(email)s,%(password)s);'
        resultado = BaseDeDatos('datos_clientes').query_db(query, data)
        return resultado

    @classmethod
    def update(cls, data):
        query = 'UPDATE usuario SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, password=%(password)s WHERE id=%(id)s ;'
        resultado = BaseDeDatos('datos_clientes').query_db(query, data)
        return resultado

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM usuario WHERE id=%(id)s;'
        resultado = BaseDeDatos('datos_clientes').query_db(query, data)
        return resultado

    @classmethod
    def read_usuario(cls, data):
        query = 'SELECT * FROM usuario WHERE id=%(id)s;'
        resultado = BaseDeDatos('datos_clientes').query_db(query, data)
        return cls(resultado[0])

    @classmethod
    def usuario_email(cls, email):
        query = 'SELECT * FROM usuario WHERE email LIKE %(email)s;'
        resultados = BaseDeDatos('datos_clientes').query_db(
            query, {'email': email})
        usuarios = []
        for resultado in resultados:
            usuarios.append(cls(resultado))
        return usuarios

    @staticmethod
    def validar_registro(datos):
        print(datos, "SI LA DATA VINO A VALIDAR")
        is_valid = True  # asumimos que esto es true
        if len(datos['nombre']) < 2:
            flash("Tu nombre debe contener al menos 3 caracteres", 'datos')
            is_valid = False
        if not SOLO_LETRAS_REGEX.match(datos['nombre']):
            flash("El nombre debe tener solo letras!", 'datos')
            is_valid = False
        if len(datos['apellido']) < 2:
            flash("Tu apellido debe contener al menos 3 caracteres.", 'datos')
            is_valid = False
        if not SOLO_LETRAS_REGEX.match(datos['apellido']):
            flash("El apellido debe tener solo letras!", 'datos')
            is_valid = False
        if not EMAIL_REGEX.match(datos['email']):
            flash("Invalid email address!", 'datos')
            is_valid = False
        if len(datos['password']) < 8:
            flash("El password debe tener al menos 8 caracteres!", 'datos')
            is_valid = False
        if datos['password'] != datos['confirmar_password']:
            flash("El password no coincide con la confirmacion!", 'datos')
            is_valid = False
        print('resultado validar: ', is_valid)
        return is_valid
