from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms
from models import db, Alumnos
from flask_migrate import Migrate
from maestros.routes import maestros
from alumnos.routes import alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
db.init_app(app)
migrate = Migrate(app, db) # Migracion a db
app.register_blueprint(maestros) #Registrar el Blueprint de maestros
app.register_blueprint(alumnos) #Registrar el Blueprint de alumnos

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()
