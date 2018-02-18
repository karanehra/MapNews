from bs4 import BeautifulSoup

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