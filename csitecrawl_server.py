from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbclass


def update():
    import time 

    from selenium import webdriver
    browser = webdriver.Chrome('./chromedriver')
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

    categories = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-htoDjs.dxFxTu > div')
    creators = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-htoDjs.dxFxTu > div')
    titles = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-gzVnrw.boJzmV')
    likes = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(1)')
    goals = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(2)')
    links = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a')

    for classes in zip(categories, creators, titles, likes, goals, links):    
        print(db.class101.find_one({'title':classes[2].text},{'_id':0}))
        if db.class101.find_one({'title':classes[2].text},{'_id':0}) != None:
            db.class101.update_many({'title':classes[2].text},{'$set':{'like':classes[3].text,'goal':classes[4].text.split('%')[0] + '%', 'link': 'class101.net' + classes[5].attrs['href']}})
        
        elif  int(classes[4].text.split('%')[0])> 100 and db.class101.find_one({'title':classes[2].text},{'_id':0}) == None:# user = db.users.find_one({'name':'bobby'},{'_id':0})
            category = classes[0].text.split('・')[0]
            creator = classes[1].text.split('・')[1]
            title = classes[2].text
            like = classes[3].text
            goal = classes[4].text.split('%')[0] + '%'
            link = 'class101.net' + classes[5].attrs['href']

            doc = {
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
