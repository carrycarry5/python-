import urllib.request
import http.cookiejar
import urllib.parse

url = "http://www.renren.com/PLogin.do"
header = {
    "User-Agent": "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)"
}
#登入需要用到的账号密码
data = {
    "email":"18379727052",
    "password":"you123456"
}
#转码
data = urllib.parse.urlencode(data).encode("utf-8")

#通过cookiejar类来创建一个cookiejar类对象用来存储cookie
cookie = http.cookiejar.CookieJar()

#通过HTTPCookieProcessor来构造一个处理器对象，用来处理cookie
#传的参数是之前构建的cookiejar对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

#构建一个自定义opener,这里的参数可以放多个handler
opener = urllib.request.build_opener(cookie_handler)

#构建一个请求
request = urllib.request.Request(url, headers=header, data=data)
#发送请求，获取响应对象，如果登入成功，生成登录后的cookie
response = opener.open(request)
print(response.read().decode("utf-8"))

