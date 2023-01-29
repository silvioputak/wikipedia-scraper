import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
import psycopg2 as dbconn
import json

# get the response in the form of html
wikiurl=" https://en.wikipedia.org/wiki/List_of_municipalities_of_Switzerland?"
table_class="wikitable sortable vcard jquery-tablesorter"
response=requests.get(wikiurl)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())

# save the dataframe as a json file
df.to_json(r'C:\Users\Pulee\Desktop\Projekti\muncipalities-scraping\Muncipalities.json')

try:
    # load json file
    f = open('Muncipalities.json')
    data = json.load(f)
    # connect to the PostgreSQL server
    conn = dbconn.connect(
        database="datamir",
        user="datamir",
        password="datamir",
        host="localhost",
        port="5435"
    )
    cursor = conn.cursor()
    #iterate through the json file and insert data into the database
    for i in data["Municipality"]:     
        result = cursor.execute("""INSERT INTO municipalities (id, municipality, canton ) VALUES (%s, %s,%s);""", (i, data["Municipality"][i],data["Canton"][i]))

    conn.commit()
    cursor.close()
    conn.close()
    f.close()


except Exception as Error:
    print(Error)

