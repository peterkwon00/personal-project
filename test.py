from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

driver.get('http://www.naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver.png')
driver.quit()
