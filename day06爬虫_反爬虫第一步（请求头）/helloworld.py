import urllib.request

url = "https://www.baidu.com/s?wd=%E6%9D%8E%E6%98%93%E5%B3%B0"
au_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}

request = urllib.request.Request(url, headers=au_headers)
response = urllib.request.urlopen(request)
http = response.read().decode("utf-8")
print(http)
