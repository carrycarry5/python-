import urllib.request
import urllib.parse

url = "http://www.baidu.com/s"
wd = urllib.parse.urlencode({"wd": "李易峰"})
furl = url + "?" + wd

user_agent = {
    "User-Agent": "Moliza"
}
request = urllib.request.Request(furl, headers=user_agent)
response = urllib.request.urlopen(request)
http = response.read().decode("utf-8")
print(http)


