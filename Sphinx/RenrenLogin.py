'''
Created on 2016-4-11
@author: young
'''
import re,requests
from bs4 import BeautifulSoup as BS
class Renren():
    loginURL = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=####"
    icodeURL = 'http://icode.renren.com/getcode.do?t=web_login&amp;rnd=Math.random()'
    origURL = 'http://www.renren.com/home'
    data = {
        'email':'####',
        'password':'####',
        'icode':'',
        'origURL':origURL
    }
    
    def get_icode(self):    //when failcode = 512
        icodef = session.get(self.icodeURL)
        with open("icode.png", 'wb') as f:
            for line in icodef.iter_content(10):
                f.write(line)
        icode = input('icode:')
        return icode
        
    def login(self):
#        self.data['icode'] = self.get_icode()
        responds = session.post(self.loginURL,self.data).text
#        print(responds)
        soup = BS(session.get(self.origURL).content)
        print(soup)
a = Renren()
session = requests.session()
a.login()
