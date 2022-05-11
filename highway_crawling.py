import requests                 #這個套件比較便捷
import urllib.request as req    #這個套件比較完整
from bs4 import BeautifulSoup
import csv
import time
from os import sep, system
from selenium import webdriver
import csv
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pandas import *


datedata = read_csv("date&time.csv")
datelist = datedata['datestring'].tolist()
timelist = datedata['timestring'][0:288].tolist()

url_init = "https://tisvcloud.freeway.gov.tw/history/vd/"
filename = "/vd_value5_"
fileattribute = ".xml.gz"

#len(datelist):
for i in range(1,3) :     
    datestring = str(int(datelist[i]))

    url_date = url_init + datestring       

    prefs = {"download.default_directory": "D:\\python\\python_git_localrepo\\Highway_Crawling\\VDdata\\{0}".format(datestring),
                 "profile.default_content_setting_values.automatic_downloads":1}

    chromeOptions = webdriver.ChromeOptions()
        
    chromeOptions.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chromeOptions)    
    
    #driver.get(url_init)

    #driver.get(url_date)

    print("In the page of {0}".format(datestring))    
    time.sleep(1)

    #len(timelist):    
    for j in range(0,len(timelist)) : 
        
        timestring = str(int(timelist[j])).zfill(4)

        url_datetime = url_date + filename + timestring + fileattribute        
        
        #driver.get(url_date)
        
        print("wating for downloading {0}".format(timestring),end = " ")
        
        #time.sleep(1)
        
        driver.get(url_datetime)
        
        print("done")

        #driver.back()

    driver.close()
    driver.quit()

    print("prepare for nextday")
    time.sleep(10)

