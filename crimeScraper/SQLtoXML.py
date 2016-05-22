import pymysql
import xml.etree.ElementTree as ET


tree=ET.parse('markers.xml')
root=tree.getroot()
conn= pymysql.connect(host='localhost',port=3306, user='root',passwd='Apples321!',db='db_crime')
cur=conn.cursor()


#FINDS ALL PREVIOUS ENTRIES
#inneficient, why not just pull directly from database
#Directly input lat/lng into  database? sql is made for sorting, could be beneficial.
for marker in root.findall('marker'):
    id= marker.find('id').text
    time=marker.find('time').text
    incident=marker.find('incident').text
    offenses= marker.find('offenses').text
    location=marker.find('location').text
    disposition=marker.find('disposition').text
    lat=marker.find('lat').text
    lng=marker.find('lng').text


    #______________________________________________________)))))))))))))___________________________


    print(offenses)
cur.execute('SELECT * FROM crimes;')
row = cur.fetchone()

while(row):
    print(row)
    row= cur.fetchone()


    # eles= data[x].split(';')
    # values= "\""+eles[0]+"\", \""+eles[1]+"\", \""+eles[2]+"\", \""+eles[3]+"\", \""+eles[4]+"\", \""+eles[5]+"\""
    # query= "INSERT INTO crimes(id, times, incident, offenses, location, disposition) VALUES ("+values+"); "
    # print(query)
    # cur.execute(query)
    # conn.commit()

conn.close()