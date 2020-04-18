from datetime import datetime

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbclass


def update():
    import time 

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
    browser.get("https://class101.net/products/preview/list")
    time.sleep(5)

    last_height = browser.execute_script("return document.body.scrollHeight")

    while True: 
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    import requests
    from bs4 import BeautifulSoup


    soup = BeautifulSoup(browser.page_source, 'html.parser')

    categories = soup.select('#wrapper > div > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4> div:nth-child(4) > div > div.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > div > div > div > div > div')
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-htoDjs.dxFxTu > div 기존
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-cpmLhU.dpVsHD.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > div > div > div.sc-jAaTju.fNCBho > div.sc-gPEVay.gyJXxX > div 바뀐것
    creators = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0 > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4 > div:nth-child(4) > div > div.InfiniteProductList__StyledGridList-sc-1m8m88g-0 > ul > li > div > div > div > div > div')
    titles = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0 > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4 > div:nth-child(4) > div > div.InfiniteProductList__StyledGridList-sc-1m8m88g-0 > ul > li > div > div > div > div')
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-gzVnrw.boJzmV 기존
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-cpmLhU.dpVsHD.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > div > div > div.sc-jAaTju.fNCBho > div.sc-jDwBTQ.gNxzfr 바뀐것 
    likes = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0 > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4 > div:nth-child(4) > div > div.InfiniteProductList__StyledGridList-sc-1m8m88g-0 > ul > li > div > div > div > div > div > div > div:nth-child(1)')
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(1) 기존
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-cpmLhU.dpVsHD.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > div > div > div.sc-jAaTju.fNCBho > div.sc-iRbamj.blSEcj > div > div > div:nth-child(1) 바뀐 것
    goals = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0 > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4 > div:nth-child(4) > div > div.InfiniteProductList__StyledGridList-sc-1m8m88g-0 > ul > li > div > div > div > div > div > div > div:nth-child(2)')
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(2) 기존
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-cpmLhU.dpVsHD.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > div > div > div.sc-jAaTju.fNCBho > div.sc-iRbamj.blSEcj > div > div > div:nth-child(2) 바뀐 것
    links = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0 > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4 > div:nth-child(4) > div > div.InfiniteProductList__StyledGridList-sc-1m8m88g-0 > ul > li > div ')
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a 기존
    #wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(4) > div > div.sc-cpmLhU.dpVsHD.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > div > div > div.sc-brqgnP.kmPBia 바뀐 것

    browser.quit()
    

    for classes in zip(categories, creators, titles, likes, goals, links):    
        if db.class101.find_one({'title':classes[2].text},{'_id':0}) != None:
            print('update')
            db.class101.update_many({'title':classes[2].text},{'$set':{'modate':datetime.today(),'like':classes[3].text,'goal':classes[4].text.split('%')[0] + '%', 'link': 'class101.net' + classes[5].attrs['href']}})
        
        elif  int(classes[4].text.split('%')[0])> 100 and db.class101.find_one({'title':classes[2].text},{'_id':0}) == None:# user = db.users.find_one({'name':'bobby'},{'_id':0})
            firstdate = datetime.today()
            modate = datetime.today()
            category = classes[0].text.split('・')[0]
            creator = classes[1].text.split('・')[1]
            title = classes[2].text
            like = classes[3].text
            goal = classes[4].text.split('%')[0] + '%'
            link = 'class101.net' + classes[5].attrs['href']

            doc = {
                'firstdate' : firstdate,
                'modate' : modate,
                'category' : category,
                'creator' : creator,
                'title' : title,
                'like' : like,
                'goal' : goal,
                'link' : link
            }
            db.class101.insert_one(doc)

@app.route('/')
def home():
    update()
    return render_template('csitecrawl_index.html')

@app.route('/class101', methods=['GET'])
def show_list():
   
    import json 
    from bson import json_util 
    class_list = list(db.class101.find()) 
    return json.dumps({'result':'success', 'msg': '이 요청은 GET!', 'data':class_list}, default=json_util.default)
        
if __name__ == '__main__':
       app.run('0.0.0.0',port=5000,debug=True)
