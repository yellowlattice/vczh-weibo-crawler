import re
import string
import sys
import os
import urllib
from bs4 import BeautifulSoup
import requests
from lxml import etree
import traceback
import time

weiboNum = 0
weibos = []
pattern = r"\d+\.?\d*"
for a in range(1, 1001, 100):
  for page in range(a, a + 99):
    url = 'http://weibo.cn/vczh?page=%d'%(page)
    html = requests.get(url, cookies = {'ALF' : '1507260850', 'H5_INDEX' : '0_all', 'H5_INDEX_TITLE' : '%E4%BB%8A%E5%A4%A9%E4%B9%9F%E6%98%AF%E4%B8%80%E5%8F%AA%E5%92%B8%E9%B1%BC%E6%A0%BC', 'M_WEIBOCN_PARAMS' : 'featurecode%3D20000320%26luicode%3D10000011%26lfid%3D1076032677042071', 'SCF' : 'AtsIwheD9yOQZgrj9PgmPrsA1WUlqebskovYaCcLCYmU6VqBdCzZjeYHDY5H7cYCGjL5saTRqwX12vXQtNe3SXI.', 'SSOLoginState' : '1505471736', 'SUB' : '_2A250v9yoDeRhGeBN71AR8CvKzjyIHXVUQ-TgrDV6PUJbkdAKLRP_kW1XywN90_FxpfZ5zA5AaM9D2LFhRg..', 'SUBP' : '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFEhWUG_s0J6K46PZ3OIlEh5JpX5o2p5NHD95Qce0BEeh5fSo-7Ws4Dqc_xi--Xi-iFiKyWi--fi-2Xi-24i--Xi-z4iKLsi--ciK.Ri-8si--Xi-zRiKn7i--fiKysi-8Wi--fiK.Ei-zRi--4i-zpi-ihi--ci-27i-ih', 'SUHB' : '0N21ayYZdwyMcY', '_T_WM' : '1237b946ce5960d8c9b3261c796c76de'}).content
    selector = etree.HTML(html)
    info = selector.xpath("//div[@class='c']")
    for i in range(1,len(info)-3):
      weiboNum = weiboNum + 1
      #微博内容
      str_t = info[i].xpath("div/span[@class='ctt']")
      weibo = str_t[0].xpath('string(.)').encode('utf-8','ignore')
      weibos.append(weibo.decode('utf-8'))
      #print '微博内容：'+ weibo
  time.sleep(300)
print(weibos)
w = open('weibovczh.txt','a',encoding= 'utf-8')
w.write(str(weibos))
w.close()
        