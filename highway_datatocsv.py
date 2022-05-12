import csv
import pandas as pd
import xml.etree.ElementTree as ET
import gzip

datedata = pd.read_csv("date&time.csv")
datelist = datedata['datestring']
timelist = datedata['timestring'][0:288]

localpath = "C:\\VDdata\\"
filename = "\\vd_value5_"
fileattribute = ".xml.gz"

taipei_id = "nfbVD-N1-S-25-I-ES-21-台北"

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(pd.Series([None]).append(timelist))

for i in range(0,5):

    datestring = str(int(datelist[i]))
    print(datestring)

    flows = pd.Series(288)
    
    for j in range(0,len(timelist)) :

        timestring = str(int(timelist[j])).zfill(4)
        
        timepath = localpath + datestring + filename + timestring + fileattribute

        with gzip.open(timepath, 'rb') as file:
            tree = ET.parse(file)
                   
        root = tree.getroot()
        Infos = root[0]

        flow = "X"

        for info in Infos:
            if info.attrib["vdid"] == taipei_id:
                flow = info[0][0].attrib["volume"]
                break
        flows[j] = flow   
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(pd.Series([datestring]).append(flows))




    

