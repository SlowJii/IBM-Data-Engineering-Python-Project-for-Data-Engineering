import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films#cite_note-3"
csv_path = r"D:\IBM-Data-Engineering-Python-Project-for-Data-Engineering\Web-Scraping\top_25_films.csv"
db_name = "Movies_25.db"
table_name = "Top_25_Movies"
#khoi tao DataFrame
df = pd.DataFrame(columns=["Film", "Year", "Rotten Tomatoes's Top 100"])

#Lay du lieu tu trang web
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

table = data.find_all('tbody')
rows = table[0].find_all('tr')
count = 0

for row in rows:
    if count < 25:
        cols = row.find_all('td')
        if len(cols) != 0:
            data_dict = {"Film": cols[1].get_text(strip = True), "Year": cols[2].get_text(strip = True), "Rotten Tomatoes's Top 100": cols[3].get_text(strip = True)}
            df1 = pd.DataFrame(data_dict, index = [0])
            df = pd.concat([df,df1], ignore_index= False)
            count += 1
    else:
        break

# Loc lay phim truoc nam 2000
df['Year'] = pd.to_numeric(df['Year'])
filtered_df = df[df['Year'] < 2000]

filtered_df.to_csv(csv_path, index = False)

conn = sqlite3.connect(db_name)
filtered_df.to_sql(table_name, conn, if_exists = 'replace', index = False)
