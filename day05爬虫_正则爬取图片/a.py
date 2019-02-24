import urllib.request
import re
import time
start_time = time.time()
j = 1
i = 0

for j in range(1):
    url = "http://piapro.jp/illust/?page=%s" % j
    request = urllib.request.urlopen(url)
    html = request.read()
    html = html.decode("utf-8")
    finders = re.findall(r'href="/t/.*?"', html)
    for str in finders:
        try:
            str = str.strip("href=\"")
            picURL = "http://piapro.jp"+str
            picRequest = urllib.request.urlopen(picURL)
            picHtml = picRequest.read()
            picHtml = picHtml.decode("utf-8")
            picFinders = re.findall(r'src="http://c1.piapro.*?\.jpg', picHtml)
            picStr = picFinders[0].strip("'src=\"")
            print(picStr)
            urllib.request.urlretrieve(picStr, filename="Y://爬虫/%s.jpg" % i)
            print(i)
        except Exception as e:
                print("%s错误了" % i)
                continue
        finally:
                i += 1

end_time = time.time()
print("进行了%s" % (end_time - start_time))
