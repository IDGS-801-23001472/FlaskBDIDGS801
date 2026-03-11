from . import alumnos

from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from alumnos.routes import alumnos, alumnos
from models import db
from models import Alumnos

@alumnos.route("/alumnos")
def alumnosIndex():
	create_form = forms.AlumnoForm(request.form)
	#ORM select * from alumnos
	alumno = Alumnos.query.all()
	return render_template("alumnos/index.html", form=create_form, alumno=alumno)

@alumnos.route("/alumnos/crear",methods=['GET','POST'])
def alumnosCrear():
	create_form = forms.AlumnoForm(request.form)
	if request.method=='POST':
		alum = Alumnos(nombre = create_form.nombre.data,
				 apellidos = create_form.apellidos.data,
				 email = create_form.email.data,
				 telefono = create_form.telefono.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.alumnosIndex'))
	return render_template("alumnos/crear.html", form=create_form)

@alumnos.route("/alumnos/modificar",methods=['GET','POST'])
def alumnosModificar():
	create_form = forms.AlumnoForm(request.form)
	if request.method=='GET':
		id = request.args.get('id')
		# select * from alumnos where id == id
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.nombre.data = str.rstrip(alum1.nombre)
		create_form.apellidos.data = alum1.apellidos
		create_form.email.data = alum1.email
		create_form.telefono.data = alum1.telefono
	if request.method=='POST':
		id = create_form.id.data
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alum1.id = id
		alum1.nombre = str.rstrip(create_form.nombre.data)
		alum1.apellidos = create_form.apellidos.data
		alum1.email = create_form.email.data
		alum1.telefono = create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alumnos.alumnosIndex'))
	return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route("/alumnos/eliminar",methods=['GET','POST'])
def alumnosEliminar():
	create_form = forms.AlumnoForm(request.form)
	if request.method=='GET':
		id = request.args.get('id')
		# select * from alumnos where id == id
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		if alum1:
			create_form.id.data = alum1.id
			create_form.nombre.data = alum1.nombre
			create_form.apellidos.data = alum1.apellidos
			create_form.email.data = alum1.email
			create_form.telefono.data = alum1.telefono
		return render_template("alumnos/eliminar.html", form=create_form)
	
	if request.method=='POST':
		id = create_form.id.data
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		if alum1:
			db.session.delete(alum1)
			db.session.commit()
		return redirect(url_for('alumnos.alumnosIndex'))
	return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route("/alumnos/detalles",methods=['GET','POST'])
def alumnosDetalles():
	create_form = forms.AlumnoForm(request.form)
	if request.method=='GET':
		id = request.args.get('id')
		# select * from alumnos where id == id
		alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id = request.args.get('id')
		nombre = alum1.nombre
		apellidos = alum1.apellidos
		email = alum1.email
		telefono = alum1.telefono
		cursos = alum1.cursos
	return render_template("alumnos/detalles.html", id=id, nombre=nombre, apellidos=apellidos, email=email, telefono=telefono, cursos=cursos)