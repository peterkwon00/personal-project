
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

# 타겟 URL을 읽어서 HTML를 받아오고,
#headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#data = requests.get('https://class101.net/products/preview/list',headers=headers)
#print(data.text)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(browser.page_source, 'html.parser')

category = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-htoDjs.dxFxTu > div')
creator = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-htoDjs.dxFxTu > div')
titles = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-gzVnrw.boJzmV')
likes = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(1)')
goals = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(2)')
links = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a')

for classes in zip(category, creator, titles, likes, goals, links):
    a = int(classes[4].text.split('%')[0])
    if  a > 100
    print(classes[0].text.split('・').[0], classes[1].text.split('・').[1], classes[2].text, classes[3].text, classes[4].text.split('%')[0] + '%', 'class101.net/' + classes[5].attrs['href'])

