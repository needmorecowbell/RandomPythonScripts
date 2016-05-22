import pymysql
myfile= open("log.txt")
conn= pymysql.connect(host='localhost',port=3306, user='root',passwd='Apples321!',db='db_crime')
cur=conn.cursor()
data=myfile.readlines()
for x in range(0,data.__len__()):

    eles= data[x].split(';')
    values= "\""+eles[0]+"\", \""+eles[1]+"\", \""+eles[2]+"\", \""+eles[3]+"\", \""+eles[4]+"\", \""+eles[5]+"\""
    query= "INSERT INTO crimes(id, times, incident, offenses, location, disposition) VALUES ("+values+"); "
    print(query)
    cur.execute(query)
    conn.commit()

conn.close()
myfile.close()