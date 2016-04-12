'''
Created on 2016-3-30
@author: young
'''
from bs4 import BeautifulSoup as BS
import requests

url = 'http://www.zhihu.com'
login_url = url+'/login/email'
captcha_url = 'http://www.zhihu.com/captcha.gif'
headers={ 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Referer': 'http://www.zhihu.com/',
'Content-Length': '154',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
'Accept-Encoding': 'gzip, deflate, sdch',
'Host':' www.zhihu.com',
'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
'Content-Type': 'application/x-www-form-urlencoded',
'Connection':' keep-alive'
}
login_data={'email':'####',#替换为账号
            'password':'####',#替换为密码
            'remember_me':'true',
            'Referer': 'http://www.zhihu.com/'
}
def add_xsrf():
    '''向login_data里面添加_xsrf值，首先获取未登录状态的响应报文，
     利用soup解析出_xsrf值'''
    
    soup=BS(requests.get(url).text)
    xsrf=soup.find('input',attrs={'name':'_xsrf'})['value']
    login_data['_xsrf'] = xsrf.encode('utf-8')
    
def add_captcha():
    captcha =session.get(captcha_url,stream=True)
    with open('captcha.gif','wb') as f:
        for line in captcha.iter_content(10):
            f.write(line)
    captcha_str = input('请输入验证码:')
    login_data['captcha'] = captcha_str




if __name__=='__main__':
    session = requests.session()
    add_xsrf()
    #add_captcha()
    responds=session.post(login_url, headers=headers, data=login_data)
    print(responds)
    soup = BS(session.get(url).text)
    #name = soup.find_all('span','name')
    #print(name)
    #print(soup)
    with open('zhihu.html','w+',encoding="utf8",errors='ignore')as f:
        print(session.get(url).text,file=f)
        
