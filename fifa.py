from selenium import webdriver
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
url = 'https://www.fifa.com/fifa-world-ranking/ranking-table/men/'
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get(url)

page = driver.page_source
fifa_rank_html_list = BeautifulSoup(page, "html.parser")
fifa_rank_list = fifa_rank_html_list.select('.fc-ranking-list-full_rankingTable__ae6FP > tbody > tr')
# print(fifa_rank_list)
for obj in fifa_rank_list:
    print(obj.find('td', {'class': 'fc-ranking-item-full_rankingTableFullCell__zA5Cr fc-ranking-item-full_rank__PYZk4'}).text, '위 : ',
          obj.find('span', {'class': 'd-none d-lg-block'}).text, '\t\t\tpoints : ',
          obj.find('div', {'class': 'd-flex ff-mr-16'}).text


          )


