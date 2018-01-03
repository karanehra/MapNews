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
        data = request.json['data']  
        length = len(data)
        address = range(0,length)
        for i in range(0,length):
            address[i] = str(data[i]['long_name'])
        print address
        query=''
        for i in range(0,len(address)):
            if not any(char.isdigit() for char in str(address[i])) and i < (len(address)-1):
                query = query + address[i] + '+'
            elif not any(char.isdigit() for char in address[i]):
                query = query + address[i]
        query = query.replace(' ', '+')
        return jsonify(get_news(query))


def get_news(query):
    print "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=nws"
    r = requests.get("https://www.google.co.in/search?q="+query+"&source=lnms&tbm=nws")
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
    news = []
    for i in range(0,len(links)):
        newsobject = {}
        newsobject["link"] = str(links[i])
        newsobject["heading"] = headings[i].encode('utf-8')
        newsobject["description"] = descripts[i].encode('utf-8')
        news.append(newsobject)
    return news