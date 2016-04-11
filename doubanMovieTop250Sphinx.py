'''
Created on 2016-3-22
@author: young
Func: Crawling Douban Movie Top250 to local db
'''
import requests, re, time
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/47.0.2526.80 Safari/537.36 QQBrowser/9.3.6872.400'}
db_path = "G:\pycharm_project\CRAWLER.db"
url = "https://movie.douban.com/top250/?start="
movie_items = []

def Sphinx():    #crawl movie list
    for page in range(10):
        src_html = requests.get(url+str(page*25), header)
        soup = BeautifulSoup(src_html.text, "html.parser")
        get_items_src = soup.find_all(class_ = "item")
        for item in get_items_src:
            item_rank = int(item.em.text)
            item_title = item.find(attrs={"class":"title"}).text    #equel to item.span.text
            item_rating = item.find(class_ = re.compile("rating_num")).text
            try:
                item_quote = item.find(class_ = "inq").text
            except AttributeError:
                item_quote = ""
            item_url = item.a["href"]
            movie_items.append([item_rank,item_title, item_rating, item_quote, item_url])

def data_2_db():    #db operator
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE MOVIE_TOP250 (rank integer PRIMARY KEY, \
                title nvarchar(800), rating varchar(3), quote text NULL, url varchar(45))")
    for item in movie_items:
        cursor.execute("INSERT INTO MOVIE_TOP250 VALUES (?,?,?,?,?)", item)    #search the official doc
    conn.commit()
#    cursor.execute("SELECT * FROM MOVIE_TOP250")
#    cursor.execute("CREATE VIEW movietop250_view AS SELECT * FROM MOVIE_TOP250")
#    cursor.execute("SELECT * FROM movietop250_view")
#    values = cursor.fetchall()
#    print(values)
    cursor.close()
    conn.close()

Sphinx()
data_2_db()
