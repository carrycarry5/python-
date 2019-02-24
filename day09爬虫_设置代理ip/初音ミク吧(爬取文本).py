import urllib.request
import re
import utils.get_ip
import utils.get_user_agent

url = "https://tieba.baidu.com/f?kw=%E5%88%9D%E9%9F%B3%E3%83%9F%E3%82%AF"
user_agent = utils.get_user_agent.getPCUA()
ip = utils.get_ip.gethttpIP()


def getHttp():
    request = urllib.request.Request(url, headers={"User-Agent": user_agent})

    # 创建一个proxyhandler处理器
    proxy_handler = urllib.request.ProxyHandler({"http": ip})
    # 创建一个opener
    opener = urllib.request.build_opener(proxy_handler)

    response = opener.open(request)

    http = response.read().decode("utf-8")
    return http

def getTitle(http):
    #<a rel="noreferrer"  href="/p/5530988994" title="2017n站v家标签的投稿统计" target
    titles = re.findall(r'<a.*?title=".*?" target', http)
    return titles

def dealTitle(titles):
    file = open("D://初音吧标题.txt", mode="w", encoding="utf-8")
    i = 1
    for t in titles:
        new_title = re.sub(r".*?href=.*?=", "", t)
        new_title = re.sub(r"target", "", new_title)
        file.write(str(i)+"."+new_title+"\n")
        i += 1
    file.close()


http = getHttp()
titles = getTitle(http)
dealTitle(titles)
