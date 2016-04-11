import requests,re,time
from bs4 import BeautifulSoup as BS


url = "http://www.dygod.info/gndy/china/"

class MovieType(object):
    items = []
    def __init__(self, type, url):
        self.type = type
        self.url = url

    def get_items(self):
        i = 29
        flag = 0
        exist = 0
        try:
            req = requests.get(self.url+'index_'+str(i)+".html", timeout = 5)
        except 'ReadTimeoutError' as e:
            print(e)
        while req.status_code == 200:
            if flag == 0:
                soup = BS(req.content,"lxml")
                for item in soup.find_all("a", "ulink"):
                    link = item.get("href")
                    for j in self.items:
                        if link==j:
                            exist = 1
                            break
                    if exist:
                        continue
                    self.items.append(link)
                    print(link)
                exist = 0
                i+=1
            try:
                req = requests.get(self.url+'index_'+str(i)+".html", timeout = 5)
                flag = 0
            except Exception as e:
                flag = 1
                print(e)
                continue
        print("Get all items!!!")

    def get_download_link(self):
        for item in self.items:
            print("doing:",item)
            def get_req():
                while(1):
                    try:
                        req = requests.get("http://www.dygod.info"+item, timeout = 5)
                        break;
                    except Exception as e:
                        print(e)
                        print("timeout:",item)
                        print("doing:",item)
                return req
            soup = BS(get_req().content,"lxml")
            for link in soup.find_all(text=re.compile("ftp")):
                print(re.search(r'(ftp.*)',link).group(0))
                with open("F://dytt/"+self.type+'.txt',"a+") as f:
                    try:
                        f.write(re.search(r'(ftp.*)',link).group(0) + "\n")
                    except UnicodeEncodeError as uerror:
                        print(uerror)
                        f.write(re.search(r'(ftp.*)',link).group(0).replace("\xa0",'')+'\n')

        print("Save all links!!!")

china = MovieType('china', url)
china.get_items()
china.get_download_link()
