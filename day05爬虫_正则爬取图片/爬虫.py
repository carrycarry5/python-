import urllib.request
import re


# f = urllib.request.urlopen("http://www.itcast.cn")
# print(f.read())
#
# f.close()

# f1 = urllib.request.urlopen("http://img1.imgtn.bdimg.com/it/u=3562270891,113833969&fm=214&gp=0.jpg")
#
# print(f1.read())

# url = "https://i0.hdslb.com/bfs/live/77493.jpg@.webp?01241110"
#
# req = urllib.request.urlretrieve(url, filename="D://tonr.jpg")

url = "https://tieba.baidu.com/index.html"
request = urllib.request.urlopen(url)
html = request.read()
html = html.decode("utf-8")

finders = re.findall(r'src="http.*?\.jpg"', html)
i = 0
for str in finders:
    i +=1
    str = str.strip("src=\"")
    try:
        urllib.request.urlretrieve(str, filename="D://爬虫/%s.jpg" % (i))
        print(i)
    except Exception as e:
        print("%s错误了"%(i))
        continue
