
import urllib.request
from bs4 import BeautifulSoup



for x in range(0,19):
    print(x)
    with urllib.request.urlopen("http://police.psu.edu/daily-crime-log?field_reported_value[value]&page="+str(x)) as url:
        s = url.read()


    tree = BeautifulSoup(s,"html.parser")
    good_html = tree.getText()
    good_html=good_html[good_html.find("Incident #:"):good_html.find("Charges/Citations:")]


    incidentArr=good_html.splitlines()



    myfile= open("log.txt","a")
    for x in range(0, incidentArr.__len__()):
        line= incidentArr[x]
        if(line.find("Incident #")!=-1):
            id=line[line.find(":")+3:line.__len__()]
            myfile.write(id)
            myfile.write(";")
        elif(line.find("Reported:")!=-1):
            timeReported = line[line.find(":") + 3:line.__len__()]
            myfile.write(timeReported)
            myfile.write(";")
        elif(line.find("Nature of the Incident:")!=-1):
            incidentNature = line[line.find(":") + 3:line.__len__()]
            myfile.write(incidentNature)
            myfile.write(";")
        elif(line.find("Offenses")!=-1):
            offenses = line[line.find(":") + 3:line.__len__()]
            myfile.write(offenses)
            myfile.write(";")
        elif(line.find("Location")!=-1):
            location = line[line.find(":") + 3:line.__len__()]
            myfile.write(location)
            myfile.write(";")
        elif(line.find("Disposition")!=-1):
            disposition = line[line.find(":") + 3:line.__len__()]
            Values= [id,timeReported,incidentNature,offenses,location,disposition]
            myfile.write(disposition)
            myfile.write("\n")





#http://www.police.psu.edu/psu-police/daily-crime-log.cfm
