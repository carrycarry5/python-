import urllib.request
from bs4 import BeautifulSoup

url  = "https://www.zhihu.com/people/edit"

headers = {
    "Connection": "keep-alive",
    "User-Agent" : "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Cookie":' q_c1=6d818c4572bc43b0a25bc289b6281c4a|1516756497000|1516756497000; _zap=b9b3794d-c926-47cd-a486-69d0bf5f71f2; l_cap_id="NTg0OGYwYWIxMDhjNGYxZjkxMjUwN2NhZjQyYjdiYWQ=|1516800254|73a7ba7b83ba8b2a56d67fc6aa5d6455e85ba53f"; r_cap_id="ZGRkNmNjOTMwMzY0NGZmYjk3MmY4ZTYzNWQwMjMyMzQ=|1516800254|a42e80b9f5b9d4a9b2271886f2879d11b5df9c66"; cap_id="OTc3OTQ0YzBkOGJkNDUyMWJlY2Q1NTUwYWJmZWJmYWY=|1516800254|56d98af22383befc5fe53ca3e017a853d02ad2d7"; aliyungf_tc=AQAAANFAQylUNwIAaqdutiDrSrBFFP7J; d_c0="AJCriJp5FQ2PTsODL7KA2G4Nf5nPyDljiwE=|1517559463"; _xsrf=fb89bb36-249f-4161-b35b-86b8b93ab4ff; capsion_ticket="2|1:0|10:1517560593|14:capsion_ticket|44:MjhjOWU0OGNhZDQwNDZjMzhkOWY5MTE5MWM4MTA1Y2I=|c67049616db3525d14843a8b955e980be5a007198f652af64f4b1623fc9bb838"'
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")
soup = BeautifulSoup(html)
html = soup.prettify()
print(html)