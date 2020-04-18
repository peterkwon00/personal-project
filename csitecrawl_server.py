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

    categories = soup.select('ul > li > a > div > div:nth-child(2) > div:nth-child(1)')
    creators = soup.select('ul > li > a > div > div:nth-child(2) > div:nth-child(1)')
    titles = soup.select('ul > li > a > div > div:nth-child(2) > div:nth-child(2)')
    likes = soup.select('ul > li > a > div > div:nth-child(2) > div:nth-child(3) > div > div > div:nth-child(1)')
    goals = soup.select('ul > li > a > div > div:nth-child(2) > div:nth-child(3) > div > div > div:nth-child(2)')
    links = soup.select('ul > li > a')


    browser.quit()
    


    for classes in zip(categories, creators, titles, likes, goals, links):    
        print(classes[0].text.split('・')[0], classes[1].text.split('・')[1], classes[2].text, classes[3].text, classes[4].text.split('%')[0], classes[5].attrs)
        if  int(classes[4].text.split('%')[0])> 100 and db.class101.find_one({'title':classes[2].text},{'_id':0}) == None:# user = db.users.find_one({'name':'bobby'},{'_id':0})
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

        if db.class101.find_one({'title':classes[2].text},{'_id':0}) != None:
            print('update')
            db.class101.update_many({'title':classes[2].text},{'$set':{'modate':datetime.today(),'like':classes[3].text,'goal':classes[4].text.split('%')[0] + '%', 'link': 'class101.net' + classes[5].attrs['href']}})

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
