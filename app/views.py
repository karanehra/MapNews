from flask import render_template, flash, redirect, request, jsonify
from app import app
from .forms import LoginForm
from bs4 import BeautifulSoup
import requests

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route("/function_route", methods=["GET", "POST"])
def my_function():
    if request.method == "POST":
        data = {}    
        data['address'] = request.json['data']
        address = {}
        address_string = str('')
        length = len(data['address'])
        for i in range(0,length):
            address["add"+str(i)] = data['address'][i]['long_name']
            address_string = address_string + str(address["add"+str(i)]) + str(' ')
        get_news(address_string)
        return jsonify(address)


def get_news(address):
    r = requests.get("https://www.google.co.in/search?q=Shire+of+East+Pilbara++Western+Australia&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjKufXizZnYAhUHso8KHULyC9wQ_AUICygC&biw=676&bih=678")
    soup = BeautifulSoup(r.text,"html.parser")   
    soup = soup.body.find("div" , id="search")
    soup = soup.find_all("div", class_="g")
    print soup[0]
