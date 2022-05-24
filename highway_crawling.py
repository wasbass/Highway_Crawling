import time
from selenium import webdriver
import pandas as pd
import os
import glob


datedata = pd.read_csv("date&time.csv")
datelist = datedata['datestring'].tolist()
timelists = datedata['timestring'][0:288].tolist()
timelist = timelists[84:120] + timelists[204:240] #只選擇上班時間和下班時間

url_init = "https://tisvcloud.freeway.gov.tw/history/vd/"
filename = "/vd_value5_"
fileattribute = ".xml.gz"


for i in range(datelist.index(20181001.0),datelist.index(20191231.0)+1) :     
    datestring = str(int(datelist[i]))

    print("wating for downloading {0}".format(datestring),end = " ")

    it_exist = os.path.exists("C:\\VDdata\\"+datestring) 

    url_date = url_init + datestring       

    prefs = {"download.default_directory": "C:\\VDdata\\{0}".format(datestring),
                 "profile.default_content_setting_values.automatic_downloads":1}

    chromeOptions = webdriver.ChromeOptions()
        
    chromeOptions.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome(options=chromeOptions)    

    start_time = 0
    
    if it_exist:
        num_of_exist_file = len(glob.glob("C:\\VDdata\\"+datestring+"\\*.gz"))

        print(num_of_exist_file ,end = " ")

        if num_of_exist_file > 65:
            start_time = num_of_exist_file
    
    for j in range(start_time,len(timelist)) :
    #for j in range(len(timelist)-1,len(timelist)) : #如果只要再下載一筆
        
        timestring = str(int(timelist[j])).zfill(4)

        url_datetime = url_date + filename + timestring + fileattribute

        if os.path.isfile("C:\\VDdata\\"+datestring+"\\"+filename + timestring + fileattribute):
            continue
        
        driver.get(url_datetime)

    time.sleep(8)

    driver.close()
    driver.quit()

    print("done")


'''
targetPattern = r"C:\\VDdata\\**\\*.crdownload"
glob.glob(targetPattern)
'''
