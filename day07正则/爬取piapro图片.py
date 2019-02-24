import re
import urllib.request
import urllib.parse
import random

user_agent = [
         "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
         "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
         "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
         "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"
    ]
headers = random.choice(user_agent)

def getHttp(url):
    # 发送请求，得到请求对象
    request = urllib.request.Request(url)
    #设置请求报头
    request.add_header("User-Agent", headers)
    # 获取响应对象
    response = urllib.request.urlopen(request)
    # 获取响应文件
    http = response.read().decode("utf-8")
    #将得到的http文件返回
    return http

def get_i_imageURL(http):
    result = re.findall(r'href="/t/.{4}', http)
    url_arr = []
    for i in result:
        url_arr.append("http://piapro.jp"+re.sub(r'href="', "", i))

    return url_arr

def get_imageURL(http):
    result = re.findall(r"http://c1\.piapro\.jp/timg.+?\.(?:png|jpg|jpeg|gif|BMP|PCX|TIFF|TGA|PNG|JPEG|JPG)", http)
    if not result[0]:
        return 0
    else:
        url = result[0]
        return url


def save_image(imageURL, page, i, extends):
    image_name = (page-1) * 30 + i
    print(image_name)
    urllib.request.urlretrieve(imageURL, "G:\piapro snowmiku2018/%s.%s" % (image_name, extends))

def piapro_spider():
    for page in range(1, 4953):
        url = "http://piapro.jp/search/?view=image&keyword=%E9%9B%AA%E3%83%9F%E3%82%AF2018&order=sd&page=" + str(page)
        http = getHttp(url)
        i_imageURLs = get_i_imageURL(http)  # 获取本页所有的图片URL
        i = 0
        for image in i_imageURLs:
            i += 1
            image_http = getHttp(image)
            imageURL = get_imageURL(image_http)
            if imageURL == 0:
                print("continue")
                continue
            save_image(imageURL, page, i, imageURL[-3:])


piapro_spider()




