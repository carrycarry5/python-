import urllib.request
import urllib.parse
import random

url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%89%A7%E6%83%85,%E7%94%B5%E5%BD%B1"
user_agent_list = [
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)",
]
form_data = {
    "start":"20"
}
form_data = urllib.parse.urlencode(form_data).encode("utf-8")

#随机获取一个用户代理
headers = random.choice(user_agent_list)
#构造一个请求
request = urllib.request.Request(url, data=form_data)
#添加请求报头
request.add_header("User-Agent", headers)
#获取响应对象
response = urllib.request.urlopen(request)
#获取响应文件
http = response.read().decode("utf-8")
#将响应内容写入本地文件
#
file = open("D://豆瓣.txt", mode="w")
file.write(http)
file.close()





