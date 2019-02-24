import urllib.request
from bs4 import BeautifulSoup

User_agent = {
    "User-Agent" : "Mozilla"
}

url = "https://tieba.baidu.com/p/5537866867"

request = urllib.request.Request(url, headers=User_agent)
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")

#html = "<div>hahahahahah</div>"

soup = BeautifulSoup(html)

imgs = soup.select(".BDE_Image")
for i in imgs:
    print(i["src"])

# strs = soup.select("div")
# for s in strs :
#     print(s.string)
