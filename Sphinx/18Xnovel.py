'''
Created on 2016-3-25
@author: young
Func: Crawling FBI warning novels
'''
import requests,urllib.request,re,json
from bs4 import BeautifulSoup as BS

url = 'http://www.84fy.com/html/article/'    #FBI Warnning website
path = 'G:\pycharm_project'    #article saving path
begin_num = '119538'    #where article id begins and ends
end_num = '214296'
articles = []

def getarticles():
    for article_id in range(int(begin_num),int(end_num)):
        article_url = url+str(article_id)+'.html'
        try:
            req = urllib.request.urlopen(article_url)    #open url and return a response code (200, 404 ect.)
            soup = BS(req ,'html.parser')    #represents the html page as a nested data structure
            article = soup.find_all('div','main')    #find <div class = 'main'> tag
            for item in article:
                article_title = item.find(class_ = 'title').string    #find <div class = 'title'> tag and extract the content
                article_title = re.sub(r'[\|/|||:|*|?|"|<|>]','',article_title)    #avoid IOError[ERROR 22], for filename can't contain those character
                article_content = item.find(class_ = 'n_bd').text    #find <div class = 'n_bd'> tag where lies text
                article_content = re.sub('\u3000','\n', article_content)    #line feed, \u3000 is blank with GBK(but differ from ' ')
                #article_content = re.sub(' ','\n', article_content)
                if len(article_content)>500 and not re.search('\d{1,3}P',article_title, re.I):    #filter most of the img and movie page
                    articles = [article_title,article_content]
                    print(articles[0])
                    dl(articles)
                else:
                    print(article_id,article_title," is not an article!!")
        except urllib.error.HTTPError as err:    #ignore 404 to continue crawl
            print(err)
def dl(article):
    fp = open(path+'/'+article[0]+'.txt', 'w', encoding='utf-8')
    fp.write(article[1])
    fp.close()
"""
def download():
    for item in articles:
        fp = open(path+'/'+item[0]+'.txt', 'w', encoding='utf-8')
        fp.write(item[1])
        fp.close()
"""
getarticles()
print('success!')
