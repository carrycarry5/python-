import urllib.request
import urllib.parse

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
key = input("请输入要翻译的文字")
headers = {
    "User-Agent": "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
}
formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt":"1516864572286",
    "sign":"0b785c96e4df555779c0897927267f84",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "ypoResult":"false"
}

data = urllib.parse.urlencode(formdata).encode(encoding="utf-8")
#构建请求对象
request = urllib.request.Request(url, data=data, headers=headers)
#获取响应对象
response = urllib.request.urlopen(request)
#获取响应文件
http = response.read().decode("utf-8")
print(http)



