import urllib.request
import urllib.parse

url = "http://www.baidu.com/baidu?"
headers = {
    "User-Agent" : "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
    "hahah" :"wojiao gu cheng lin"
}

wd = urllib.parse.urlencode({"wd":"李易峰"})
fullurl = url + wd


#构造请求对象
request = urllib.request.Request(fullurl, headers=headers)
#获取响应对象
response = urllib.request.urlopen(request)
#获取响应文件
http = response.read().decode("utf-8")
print(http)
