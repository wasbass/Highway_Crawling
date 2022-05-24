import csv
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import gzip
import os


datedata = pd.read_csv("date&time.csv")
datelist = datedata['datestring']
timelists = datedata['timestring'][0:288].tolist()
timelist  = timelists[84:120] + timelists[204:240]

localpath = "C:\\VDdata\\"
filename = "\\vd_value5_"
fileattribute = ".xml.gz"

#donhu_id   = "nfbVD-N1-S-15-I-WS-1-東湖"  #單線道入口
neihu_id   = "nfbVD-N1-S-16.298-M-LOOP"  #雙線道入口
#nfbVD-N1-S-16-I-WS-1-內湖
yunsan_id  = "nfbVD-N1-S-23-I-ES-2C-圓山" #雙線道入口
taipei_id  = "nfbVD-N1-S-25-I-ES-21-台北" #雙線道入口
nangon_id  = "nfbVD-N3-S-16-I-ES-1-南港系統"
muzha_id   = "nfbVD-N3-S-20-I-WS-1-木柵"


with open('neihu.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([None] + timelist)

with open('yunsan.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([None] + timelist)

with open('taipei.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([None] + timelist)

with open('nangon.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([None] + timelist)

with open('muzha.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([None] + timelist)


start_day = 0
end_day   = 1094 #1094


for i in range(start_day,end_day):

    datestring = str(int(datelist[i]))
    print(datestring , end = "")

    neihu_flows  = pd.Series(len(timelist))
    yunsan_flows = pd.Series(len(timelist))
    taipei_flows = pd.Series(len(timelist))
    nangon_flows = pd.Series(len(timelist))
    muzha_flows  = pd.Series(len(timelist))
    
    for j in range(0,len(timelist)) :

        timestring = str(int(timelist[j])).zfill(4)        
        
        timepath = localpath + datestring + filename + timestring + fileattribute

        flow = list(np.repeat("X",5))

        if os.path.isfile(timepath):
            try:
                with gzip.open(timepath, 'rb') as file:
                    tree = ET.parse(file)
            except:
                neihu_flows [j] = flow[0]
                yunsan_flows[j] = flow[1]
                taipei_flows[j] = flow[2]
                nangon_flows[j] = flow[3]
                muzha_flows [j] = flow[4]
                continue
        else:
            neihu_flows [j] = flow[0]
            yunsan_flows[j] = flow[1]
            taipei_flows[j] = flow[2]
            nangon_flows[j] = flow[3]
            muzha_flows [j] = flow[4]
            continue
                   
        root = tree.getroot()
        Infos = root[0]

        
        catch = 0
        for info in Infos:
            if info.attrib["vdid"] == neihu_id:
                flow[0] = info[0][0].attrib["volume"]
                catch += 1
            elif info.attrib["vdid"] == yunsan_id:
                flow[1] = info[0][0].attrib["volume"]
                catch += 1
            elif info.attrib["vdid"] == taipei_id:
                flow[2] = info[0][0].attrib["volume"]
                catch += 1            
            elif info.attrib["vdid"] == nangon_id:
                flow[3] = info[0][0].attrib["volume"]
                catch += 1
            elif info.attrib["vdid"] == muzha_id :
                flow[4] = info[0][0].attrib["volume"]
                catch += 1

            if catch >= 5:
                break
                
        neihu_flows [j] = flow[0]
        yunsan_flows[j] = flow[1]
        taipei_flows[j] = flow[2]
        nangon_flows[j] = flow[3]
        muzha_flows [j] = flow[4]
        
    with open('neihu.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(pd.Series([datestring]).append(neihu_flows))

    with open('yunsan.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(pd.Series([datestring]).append(yunsan_flows))

    with open('taipei.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(pd.Series([datestring]).append(taipei_flows))

    with open('nangon.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(pd.Series([datestring]).append(nangon_flows))

    with open('muzha.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(pd.Series([datestring]).append(muzha_flows))

    print("done")



        




    

