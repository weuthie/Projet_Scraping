from flask import Flask , render_template
from sqlalchemy import false

scrap = Flask(__name__)
scrap.config['SECRET_KEY'] = 'groupe4'
scrap.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe4:test123@localhost/scraping'
scrap.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false

@scrap.route('/')
def index():
    return render_template('index.html')

@scrap.route('/iphone6/')
def iphone6():
    return render_template('iphone6.html')

@scrap.route('/iphone7/')
def iphone7():
    return render_template('iphone7.html')

@scrap.route('/iphone8/')
def iphone8():
    return render_template('iphone8.html')

@scrap.route('/iphonex/')
def iphonex():
    return render_template('iphonex.html')

@scrap.route('/iphone11/')
def iphone11():
    return render_template('iphone11.html')

@scrap.route('/iphone12/')
def iphone12():
    return render_template('iphone12.html')

@scrap.route('/iphone13/')
def iphone13():
    return render_template('iphone13.html')

scrap.run(debug=True , port=8000)

