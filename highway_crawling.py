import time
from selenium import webdriver
import pandas as pd


datedata = read_csv("date&time.csv")
datelist = datedata['datestring'].tolist()
timelist = datedata['timestring'][0:288].tolist()

url_init = "https://tisvcloud.freeway.gov.tw/history/vd/"
filename = "/vd_value5_"
fileattribute = ".xml.gz"

#len(datelist):
for i in range(4,30) :     
    datestring = str(int(datelist[i]))

    url_date = url_init + datestring       

    prefs = {"download.default_directory": "C:\\VDdata\\{0}".format(datestring),
                 "profile.default_content_setting_values.automatic_downloads":1}

    chromeOptions = webdriver.ChromeOptions()
        
    chromeOptions.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chromeOptions)    
    
    #driver.get(url_init)

    #driver.get(url_date)

    print("wating for downloading {0}".format(datestring),end = " ")  
    time.sleep(1)

    #len(timelist):    
    for j in range(0,len(timelist)) : 
        
        timestring = str(int(timelist[j])).zfill(4)

        url_datetime = url_date + filename + timestring + fileattribute         
        
        #driver.get(url_datetime)

    driver.close()
    driver.quit()

    print("done")
    time.sleep(10)

