from bs4 import BeautifulSoup as soup
import requests
import cgi
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
import json
import unittest, time, re

from player_data import index_spider 
a = index_spider("Google.com")
class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("F:\exec\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.premierleague.com/players"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        #driver.find_element_by_link_text("All").click()
        for i in range(1,10):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html_source = driver.page_source
            page_soup = soup(html_source , "html.parser")
            x = page_soup.findAll('a',{'class':'playerName'})
            page_list = np.array(str(x))
            #for link in x:
	        #    print (link['href'])
            time.sleep(4)
        count = 0
        data = html_source.encode('utf-8')
        a = {}
        for link in x:
            a[count] = link['href']
            count = count + 1
            #print ("Count: " + str(count))
        #print (a)
        player_link = json.dumps(a)
        with open("player_list.json", "w") as f:
            f.write(player_link)
        #print (page_list)
        #print ("The number of players: "+ str(x))
        #print ("The number of players: "+ str(page_list))

if __name__ == "__main__":
    unittest.main()
    