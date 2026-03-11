from wtforms import Form
from flask_wtf import Form

from wtforms import StringField, IntegerField, SelectField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre=StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese nombre valido")
    ])
    apellidos=StringField("APaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno=StringField("AMaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])

class AlumnoForm(Form):
    id=IntegerField('Id',
    [validators.number_range(min=1, max=20, message="valor no valido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4, max=20, message="requiere min=4 max=20")
    ])
    apellidos=StringField('Apellidos', [
        validators.DataRequired(message="El apellido es requerido")
    ])
    email=EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])
    telefono=StringField('Telefono', [
        validators.DataRequired(message="El telefono es requerido")
    ])

class MaestroForm(Form):
    matricula=IntegerField('Matricula',
    [validators.number_range(min=1, max=20, message="valor no valido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4, max=20, message="requiere min=4 max=20")
    ])
    apellidos=StringField('Apellidos', [
        validators.DataRequired(message="El apellido es requerido")
    ])
    especialidad=StringField('Especialidad', [
        validators.DataRequired(message="La especialidad es requerido")
    ])
    email=EmailField('Correo', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])

class CursoForm(Form):
    id=IntegerField('Id',
    [validators.number_range(min=1, max=20, message="valor no valido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4, max=20, message="requiere min=4 max=20")
    ])
    descripcion=StringField('Descripcion', [
        validators.DataRequired(message="La descripcion es requerida")
    ])
    maestro_id = SelectField(
        'Maestro',
        coerce=int,
        validators=[validators.DataRequired(message="Selecciona un maestro")]
    )

class InscripcionForm(Form):
    curso_id = SelectField('Curso', coerce=int, validators=[validators.DataRequired()])
    alumno_id = SelectField('Alumno', coerce=int, validators=[validators.DataRequired()])