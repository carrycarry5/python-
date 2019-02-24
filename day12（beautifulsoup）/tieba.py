import urllib.request
from bs4 import BeautifulSoup

url = "https://tieba.baidu.com/f?kw=%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF&fr=index"

User_agent  = {
    "User-Agent" : "mozilla"
}

request = urllib.request.Request(url, headers=User_agent)

response = urllib.request.urlopen(request)

html = response.read().decode("utf-8")

soup = BeautifulSoup(html)

# imgs = soup.select("a[class='thumbnail vpic_wrap'] img")
#
# for i in imgs :
#     print(i["bpic"])

strs = soup.select("a[class='j_th_tit '] ")
for s in strs:
    print(s.string)