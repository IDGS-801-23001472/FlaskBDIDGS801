from . import cursos

from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from cursos.routes import cursos, cursos
from models import Maestros, db
from models import Curso

@cursos.route("/cursos")
def cursosIndex():
	create_form = forms.CursoForm(request.form)
	#ORM select * from cursos
	curso = Curso.query.all()
	return render_template("cursos/index.html", form=create_form, curso=curso)

@cursos.route("/cursos/crear",methods=['GET','POST'])
def cursosCrear():
	create_form = forms.CursoForm(request.form)
	create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
	if request.method=='POST':
		curs = Curso(nombre = create_form.nombre.data,
				 descripcion = create_form.descripcion.data,
				 maestro_id = create_form.maestro_id.data)
		db.session.add(curs)
		db.session.commit()
		return redirect(url_for('cursos.cursosIndex'))
	return render_template("cursos/crear.html", form=create_form)

@cursos.route("/cursos/modificar",methods=['GET','POST'])
def cursosModificar():
	create_form = forms.CursoForm(request.form)
	create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
	if request.method=='GET':
		id = request.args.get('id')
		# select * from cursos where id == id
		curs = db.session.query(Curso).filter(Curso.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.nombre.data = str.rstrip(curs.nombre)
		create_form.descripcion.data = curs.descripcion
		create_form.maestro_id.data = curs.maestro_id
	if request.method=='POST':
		id = create_form.id.data
		curs = db.session.query(Curso).filter(Curso.id==id).first()
		curs.id = id
		curs.nombre = str.rstrip(create_form.nombre.data)
		curs.descripcion = create_form.descripcion.data
		curs.maestro_id = create_form.maestro_id.data
		db.session.add(curs)
		db.session.commit()
		return redirect(url_for('cursos.cursosIndex'))
	return render_template("cursos/modificar.html", form=create_form)

@cursos.route("/cursos/eliminar",methods=['GET','POST'])
def cursosEliminar():
	create_form = forms.CursoForm(request.form)
	create_form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
	if request.method=='GET':
		id = request.args.get('id')
		# select * from cursos where id == id
		curs = db.session.query(Curso).filter(Curso.id==id).first()
		if curs:
			create_form.id.data = curs.id
			create_form.nombre.data = curs.nombre
			create_form.descripcion.data = curs.descripcion
			create_form.maestro_id.data = curs.maestro_id
		return render_template("cursos/eliminar.html", form=create_form)
	
	if request.method=='POST':
		id = create_form.id.data
		curs = db.session.query(Curso).filter(Curso.id==id).first()
		if curs:
			db.session.delete(curs)
			db.session.commit()
		return redirect(url_for('cursos.cursosIndex'))
	return render_template("cursos/modificar.html", form=create_form)

@cursos.route("/cursos/detalles",methods=['GET','POST'])
def cursosDetalles():
	create_form = forms.CursoForm(request.form)
	if request.method=='GET':
		id = request.args.get('id')
		# select * from cursos where id == id
		curso = db.session.query(Curso).filter(Curso.id==id).first()
		id = request.args.get('id')
		alumno = curso.alumnos;
	return render_template("cursos/detalles.html", curso=curso)