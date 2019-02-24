import urllib.request
import urllib.parse

def writePage(filename, html):
    with open(filename, "w" ,encoding="utf-8") as f:
        f.write(html)


def loadPage(url, filename):
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
    }
    #构造一个请求
    request = urllib.request.Request(url, headers=headers)
    #获取响应对象
    response = urllib.request.urlopen(request)
    #返回获取到的响应文件
    return response.read().decode("utf-8")

def tiebaSpider(beginPage, endPage, url):
    for page in range(beginPage, endPage+1):
        pn = (page-1) * 50
        fullurl = url + "&pn=" + str(pn)
        filename = "D://第" + str(page) +"页.html"
        html = loadPage(fullurl, filename)
        writePage(filename, html)

def test():
    tiebaName = input("请输入贴吧的名字:")
    beginPage = int(input("请输入起始页:"))
    endPage = int(input("请输入结束页:"))

    url = "https://tieba.baidu.com/f?"
    url = url + urllib.parse.urlencode({"kw" : tiebaName})
    tiebaSpider(beginPage, endPage, url)


test()
