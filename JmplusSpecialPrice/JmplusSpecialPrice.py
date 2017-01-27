#-*- coding: utf-8 -*-　
import sys
import requests
import re
from  bs4 import BeautifulSoup


msg= ''
res  = requests.get('http://class.ruten.com.tw/user/index00.php?s=jmplus01&d=4797150&o=0&m=1')
res.encoding ='utf-8' 

soup =BeautifulSoup(res.text , "html.parser") 
pattern = re.compile('【(.*)】')

for entry in soup.select('.rt-store-goods-disp-mix'):
    msg+= str(( pattern.findall(entry.select('.item-name')[0].text), 
              entry.select('.item-direct-price')[0].text[7:].replace(' ', '')))



print(msg)


