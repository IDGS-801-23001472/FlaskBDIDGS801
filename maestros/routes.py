from . import maestros

from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from maestros.routes import maestros, maestros
from models import db
from models import Alumnos, Maestros

@maestros.route("/maestros", methods=['GET','POST'])
def maestrosIndex():
    create_form=forms.MaestroForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/index.html", form=create_form,
                           maestros=maestros)

@maestros.route("/maestros/crear",methods=['GET','POST'])
def maestrosCrear():
	create_form = forms.MaestroForm(request.form)
	if request.method=='POST':
		maes = Maestros(nombre = create_form.nombre.data,
				 apellidos = create_form.apellidos.data,
				 especialidad = create_form.especialidad.data,
				 email = create_form.email.data)
		db.session.add(maes)
		db.session.commit()
		return redirect(url_for('maestros.maestrosIndex'))
	return render_template("maestros/crear.html", form=create_form)

@maestros.route("/maestros/modificar",methods=['GET','POST'])
def maestrosModificar():
	create_form = forms.MaestroForm(request.form)
	if request.method=='GET':
		matricula = request.args.get('matricula')
		# select * from maestros where matricula == matricula
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data = request.args.get('matricula')
		create_form.nombre.data = str.rstrip(maes1.nombre)
		create_form.apellidos.data = maes1.apellidos
		create_form.especialidad.data = maes1.especialidad
		create_form.email.data = maes1.email
	if request.method=='POST':
		matricula = create_form.matricula.data
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		maes1.matricula = matricula
		maes1.nombre = str.rstrip(create_form.nombre.data)
		maes1.apellidos = create_form.apellidos.data
		maes1.especialidad = create_form.especialidad.data
		maes1.email = create_form.email.data
		db.session.add(maes1)
		db.session.commit()
		return redirect(url_for('maestros.maestrosIndex'))
	return render_template("maestros/modificar.html", form=create_form)

@maestros.route("/maestros/eliminar",methods=['GET','POST'])
def maestrosEliminar():
	create_form = forms.MaestroForm(request.form)
	if request.method=='GET':
		matricula = request.args.get('matricula')
		# select * from maestros where matricula == matricula
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		if maes1:
			create_form.matricula.data = maes1.matricula
			create_form.nombre.data = maes1.nombre
			create_form.apellidos.data = maes1.apellidos
			create_form.especialidad.data = maes1.especialidad
			create_form.email.data = maes1.email
		return render_template("maestros/eliminar.html", form=create_form)
	
	if request.method=='POST':
		matricula = create_form.matricula.data
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		if maes1:
			db.session.delete(maes1)
			db.session.commit()
		return redirect(url_for('maestros.maestrosIndex'))
	return render_template("maestros/modificar.html", form=create_form)

@maestros.route("/maestros/detalles",methods=['GET','POST'])
def maestrosDetalles():
	create_form = forms.MaestroForm(request.form)
	if request.method=='GET':
		matricula = request.args.get('matricula')
		# select * from alumnos where matricula == matricula
		maes1 = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula = request.args.get('matricula')
		nombre = maes1.nombre
		apellidos = maes1.apellidos
		especialidad = maes1.especialidad
		email = maes1.email
	return render_template("maestros/detalles.html", matricula=matricula, nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"