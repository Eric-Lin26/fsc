import requests
from bs4 import BeautifulSoup
import time

def fsc():
    url = 'http://www.focus-sport.club.tw/forumdisplay.php?fid=670&page='
    i = 1 # 第幾頁
    domain = 'http://www.focus-sport.club.tw/'

    for page in range(5): # 爬5頁
        print('第', i,'頁')
        req = requests.get(url + str(i))
        req.encoding = 'utf-8' # FSC需要編碼
        if req.status_code == 200: # 測試有無錯誤
            print('連結成功')
        else:
            print('URL連結錯誤：', url)

        soup = BeautifulSoup(req.text, 'html5lib')
        titles = soup.find_all('a', class_="subject") # 搜尋a標籤, 屬性class_='subject'
        for title in titles:
            purl = title.get('href')
            print(title.text, '：', domain + purl)
            time.sleep(2)
        i += 1 # 換頁
    time.sleep(3)

fsc()
