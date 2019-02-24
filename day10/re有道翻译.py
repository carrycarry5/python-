import urllib.request
import lxml
import re
import urllib.parse

import utils.changeFormData
import utils.get_ip
import utils.get_user_agent

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
ip = utils.get_ip.gethttpIP()
user_agent = utils.get_user_agent.getPCUA()
str = input("请输入要翻译的内容:")
data = {
    "i": str,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1517191248359",
    "sign":"9d15d2a27aca491c2ac0b78121564147",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
}
data = urllib.parse.urlencode(data).encode("utf-8")

#设置proxy_handler
proxy_handler = urllib.request.ProxyHandler({"http" : ip})

#构造一个自定义opener
opener = urllib.request.build_opener(proxy_handler)

request = urllib.request.Request(url, data=data)

response = opener.open(request)

json = response.read().decode("utf-8")

print(json)





