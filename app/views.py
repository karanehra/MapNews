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
    address = address.split(" ")
    address.pop()
    query = ''
    for i in range(0,len(address)):
        print address[i]
        if i < (len(address) - 1) and address[i] != '':
            query = query+str(address[i])+'+'
        if i == (len(address)-1) and address[i] != '':
            query = query + str(address[i])
    print "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjKufXizZnYAhUHso8KHULyC9wQ_AUICygC&biw=676&bih=678"
    r = requests.get("https://www.google.co.in/search?q="+query+"&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjKufXizZnYAhUHso8KHULyC9wQ_AUICygC&biw=676&bih=678")
    soup = BeautifulSoup(r.text,"html.parser")   
    soup = soup.body.find("div" , id="search")
    soup = soup.find_all("div", class_="g")
    # print soup[0].find("div",class_="st")
    links =[]
    headings = []
    descripts = []
    for obj in soup:
        link = obj.find_all("a")
        link = link[0]
        heading = link.text
        link = link['href']
        link = link.split("=")[1]
        link = link.split("&")[0]
        descript = obj.find("div",class_="st").text
        descripts.append(descript)
        links.append(link)
        headings.append(heading)
    print headings