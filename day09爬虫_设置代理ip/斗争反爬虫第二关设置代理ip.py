import urllib.request

#构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器ip+port
http_proxyHandler = urllib.request.ProxyHandler({"http":"118.81.71.180:9797"})
#当代理ip需要账号密码授权时：
#http_proxyHandler = urllib.request.ProxyHandler({"http":"账号:密码@ip:port"})

#构建一个opener
opener = urllib.request.build_opener(http_proxyHandler)

#构造一个request请求对象
request = urllib.request.Request("http://www.baidu.com")
#接收响应对象
response  = opener.open(request)
#获取响应文件
http = response.read().decode("utf-8")
print(http)