from flask import render_template, flash, redirect, request, jsonify
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title = "SignIn", form = form)

@app.route('/receiver', methods = ['POST'])
def worker():
    # read json + reply
    data = request.get_json()
    print data
    return data 

@app.route("/function_route", methods=["GET", "POST"])
def my_function():
    if request.method == "POST":
        data = {}    
        data['data'] = request.json['data']

        return jsonify(data)
