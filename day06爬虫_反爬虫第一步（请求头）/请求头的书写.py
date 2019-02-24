import urllib.request

#通过urllib.request.Request()创建一个请求对象
url = "https://www.baidu.com/"
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}
request = urllib.request.Request(url, headers=ua_headers)

#向指定的url地址发送请求，并接受服务器响应的类文件对象
response = urllib.request.urlopen(request)
#read()方法读取文件里的所有信息，并返回字符串

# html = response.read().decode("utf-8")
#
# print(html)

#返回http的响应码
print(response.getcode())

#返回实际数据的实际URL，防止重定向
print(response.geturl())

#放回服务器响应的http报头
print(response.info())

# import urllib.request
# import random
#
# url = "https://www.baidu.com/"
# au_list = [
#     "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
#     "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
#     "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
# ]
#
# #在列表中随机选择一个user-agent
# user_agent = random.choice(au_list)
# #构造一个请求
# request = urllib.request.Request(url)
# #添加请求报头
# request.add_header("User-Agent", user_agent)
# #获取请求报头，注意首字母一定大写，其他一定小写
# print(request.get_header("User-agent"))





