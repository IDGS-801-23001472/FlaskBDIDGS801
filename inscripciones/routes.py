from . import inscripciones

from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from inscripciones.routes import inscripciones, inscripciones
from models import Curso, db
from models import Alumnos, db
from models import Inscripcion

@inscripciones.route("/inscribir",methods=['GET','POST'])
def inscribirCrear():
	create_form = forms.InscripcionForm(request.form)
	create_form.curso_id.choices = [(c.id, f"{c.nombre}") for c in Curso.query.all()]
	create_form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apellidos}") for a in Alumnos.query.all()]
	if request.method=='POST':
		insc = Inscripcion(curso_id = create_form.curso_id.data,
				 alumno_id = create_form.alumno_id.data)
		curso_id = create_form.curso_id.data
		alumno_id = create_form.alumno_id.data
		if db.session.query(Inscripcion).filter(
            Inscripcion.curso_id == curso_id,
            Inscripcion.alumno_id == alumno_id
        ).first():
			flash("El alumno ya está inscrito en este curso", "warning")
			return render_template("inscripciones/crear.html", form=create_form)
		db.session.add(insc)
		db.session.commit()
		return redirect(url_for('alumnos.alumnosIndex'))
	return render_template("inscripciones/crear.html", form=create_form)