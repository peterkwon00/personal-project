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

    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    db = client.dbclass

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    category = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-htoDjs.dxFxTu > div')
    titles = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-gzVnrw.boJzmV')
    likes = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(1)')
    goals = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a > div > div.sc-bZQynM.bOrPFB > div.sc-dnqmqq.bDsesi > div > div > div:nth-child(2)')
    links = soup.select('#wrapper > div.pages__Body-sc-1xw23vo-0.dGxVjn > main > div > div > div.PreviewProductListViewController__ListContainer-cl9x62-4.eMbZwQ > div:nth-child(3) > div > div.sc-dymIpo.kdtjOQ.InfiniteProductList__StyledGridList-sc-1m8m88g-0.kTFhbd > ul > li > a')

    for classes in zip(category, titles, likes, goals, links):
        print(classes[0].text, classes[1].text, classes[2].text, classes[3].text, classes[4].attrs['href'])

