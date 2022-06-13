from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

scrap = Flask(__name__)
scrap.config['SECRET_KEY'] = 'groupe4'
scrap.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe4:test123@localhost/scraping'
scrap.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false

db = SQLAlchemy(scrap)


class Limarket(db.Model):
    li_marketid = db.Column(db.Integer(),primary_key=True)
    li_name = db.Column(db.String(255),nullable=False)
    li_prix = db.Column(db.String(255),nullable = False)
    li_etat = db.Column(db.String(255),default="non specifier")
    li_image = db.Column(db.String(2000),nullable=False)
    
class Soumary(db.Model):
    soumary_id = db.Column(db.Integer(),primary_key=True)
    soumary_name = db.Column(db.String(255),nullable=False)
    soumary_prix = db.Column(db.String(255),nullable = False)
    soumary_etat = db.Column(db.String(255),default="non specifier")
    soumary__image = db.Column(db.String(2000),nullable=False)

class Jiji(db.Model):
    ji_id = db.Column(db.Integer(),primary_key=True)
    ji_name = db.Column(db.String(255),nullable=False)
    ji_prix = db.Column(db.String(255),nullable = False)
    ji_etat = db.Column(db.String(255),default="non specifier")
    ji_image = db.Column(db.String(2000),nullable=False)

