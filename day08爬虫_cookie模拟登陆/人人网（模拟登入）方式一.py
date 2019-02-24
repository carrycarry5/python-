import urllib.request

url = "http://zhibo.renren.com/top"

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "anonymid=jcx1u7b02hnz9w; depovince=JX; _r01_=1; JSESSIONID=abcppiDm7rBIydTcjQ2ew; ick=41d747aa-8b0f-40c1-aab1-ef2c9c5efff2; XNESSESSIONID=8ab9b95e0933; WebOnLineNotice_963562059=1; jebe_key=af96a6d9-c3a2-4aeb-b299-5bf3aa8c1010%7C77f04cb2e2a21a62280d177621e03be3%7C1517041480955%7C1%7C1517041482818; jebecookies=39783ceb-a368-46f4-8271-fd99652d0652|||||; ick_login=71fdc55f-917c-4d89-a2d5-4c00bf0378a7; _de=0D15033134124E0C59F3D78F76D1408F; p=1fb0f42a0f08ec8ce59151603e09725c9; ap=963562059; first_login_flag=1; ln_uact=18379727052; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=d8935cf50e30431416d2160b88ef7a9e9; societyguester=d8935cf50e30431416d2160b88ef7a9e9; id=963562059; xnsid=c946adef; loginfrom=syshome; ch_id=10016; wp_fold=0"
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
http = response.read().decode("utf-8")
print(http)
