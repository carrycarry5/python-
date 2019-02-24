import urllib.request
import utils.get_ip
import utils.get_user_agent
import http.cookiejar
import urllib.parse
import lxml.etree

url = "http://www.renren.com/PLogin.do"

data = {
    "email": "18379727052",
    "password": "you123456"
}
data = urllib.parse.urlencode(data).encode("utf-8")

headers = {
    "Host": "zhibo.renren.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Referer": "http://zhibo.renren.com/top",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
}

cookiejar = http.cookiejar.CookieJar()

cookie_handler = urllib.request.HTTPCookieProcessor(cookiejar)

proxy_handler = urllib.request.ProxyHandler({"https": "118.81.71.131:9797"})

opener = urllib.request.build_opener(cookie_handler)

request = urllib.request.Request(url, headers=headers, data=data)

response = opener.open(request)

html = response.read().decode("utf-8")

#解析html文件为html Dom文档
xml = lxml.etree.HTML(html)
#返回所有匹配成功的结果   xpath相当于findall()
link_list = xml.xpath("//img[@class='poster']/@src")

i = 0
for img in link_list:
    print(img)
    i += 1
    urllib.request.urlretrieve(img, "D://img/%s.jpg"%(i))