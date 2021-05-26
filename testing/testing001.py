# based on sel-dongju.py

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://gall.dcinside.com/mgallery/board/lists/?id=istp"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# #mw-content-text 바로 아래에 있는
# ul 태그 바로 아래에 있는
# li 태그 아래에 있는
# a 태그를 모두 선택합니다
# a_list = soup.select("#mw-content-text > div > ul > li a")
a_list = soup.select_one("content_box r_timebest > div > ul > li a")


for a in a_list:
    name = a.string
    print('-', name)
