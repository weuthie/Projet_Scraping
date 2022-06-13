from flask import Flask , render_template
from sqlalchemy import false
from createdb import db
from requete import Recu_info

scrap = Flask(__name__)
scrap.config['SECRET_KEY'] = 'groupe4'
scrap.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe4:test123@localhost/scraping'
scrap.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false

@scrap.route('/')
def index():
    return render_template('index.html')

@scrap.route('/iphone6/')
def iphone6():
    produits=Recu_info("iphone 6")
    return render_template('iphone6.html',limarke=produits[0],jiji=produits[1],soumari=produits[2])

@scrap.route('/iphone7/')
def iphone7():
    produits=Recu_info("iphone 7")
    return render_template('iphone7.html',limarke=produits[0],jiji=produits[1],soumari=produits[2])

@scrap.route('/iphone8/')
def iphone8():
    produits=Recu_info("iphone 8")
    return render_template('iphone8.html',limarke=produits[0],jiji=produits[1],soumari=produits[2])

@scrap.route('/iphonex/')
def iphonex():
    produits=Recu_info("iphone x")
    return render_template('iphonex.html',limarke=produits[0],jiji=produits[1],soumari=produits[2])

@scrap.route('/iphone11/')
def iphone11():
    produits=Recu_info("iphone 11")
    return render_template('iphone11.html',limarke=produits[0],jiji=produits[1],soumari=produits[2])

@scrap.route('/iphone12/')
def iphone12():
    produits=Recu_info("iphone 12")
    return render_template('iphone12.html',limarke=produits[0],jiji=produits[1],soumari=produits[2])

@scrap.route('/iphone13/')
def iphone13():
    produits=Recu_info("iphone 13")
    return render_template('iphone13.html',limarke=produits[0],jiji=produits[1],soumari=produits[2])

db.init_app(scrap)
scrap.run(debug=True , port=8000)