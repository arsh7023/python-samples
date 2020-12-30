from flask import Flask, url_for
from flask import render_template



#create an instance of class Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    #url_for('static', filename='style.css')
    return render_template('hello.html', name=name)