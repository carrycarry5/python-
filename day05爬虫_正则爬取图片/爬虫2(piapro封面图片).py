import urllib.request
import re
import time
start_time = time.time()
j = 1
i = 0

for j in range(20):
    url = "http://piapro.jp/illust/?page=%s" % j
    request = urllib.request.urlopen(url)
    html = request.read()
    html = html.decode("utf-8")
    finders = re.findall(r'url.*?\.jpg', html)
    for str in finders:
        i += 1
        str = str.strip("url(")
        str = str.strip("src=\"")
        try:
            urllib.request.urlretrieve(str, filename="D://爬虫/%s.jpg" % i)
            print(i)
        except Exception as e:
            print("%s错误了" % i)
            continue

end_time = time.time()
print("进行了%s" % (end_time - start_time))
