import re


# print("http:\\")

#匹配出，一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
# s = "A"
# print(re.match("[A-Z][a-z]*", s))

#匹配出，变量名是否有效
# s = "_name"
# print(re.match("[a-zA-Z_]\w*", s))

#匹配出，0到99之间的数字
# s = ""
# print(re.match("[1-9]?[0-9]", s))

#匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
# s = "1ad12f23s34455ff66"
# print(re.match("\w{8,20}", s))

#匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
# s = "10ss0@163.com              12344124@qq.com  1test@gmail.com"
# print(re.findall("1\w{4,20}@(?:163|qq|gmail)\.com", s))

# print(re.findall("(?:[^-]*)-(?:\d+)","010-12345678"))

# s = "<html><h1>www.itcast.cn</h1></html>"
# # print(re.match(r"<(\w*)><(\w*)>.*</\2></\1>", s))
# print(re.match(r"<(?P<n1>\w*)><(?P<n2>\w*)>.*</(?P=n2)></(?P=n1)>", s))
# r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>"

# s = '''
# <div>
#         <p>岗位职责：</p>
# <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
# <p><br></p>
# <p>必备要求：</p>
# <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
# <p>&nbsp;<br></p>
# <p>技术要求：</p>
# <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
# <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
# <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
# <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
# <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
# <p>&nbsp;<br></p>
# <p>加分项：</p>
# <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
#
#         </div>'''
#
# print(re.sub("<.*?>", "", s))


# s = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.png" style="display: inline;">'
# print(re.findall(r"http.+?\.(?:jpg|png)", s))

# s = '''
# http://www.interoem.com/messageinfo.asp?id=35
# http://3995503.com/class/class09/news_show.asp?id=14
# http://lib.wzmc.edu.cn/news/onews.asp?id=769
# http://www.zy-ls.com/alfx.asp?newsid=377&id=6
# http://www.fincm.com/newslist.asp?id=415'''
#
# new_s = re.findall(r"http://.+?\.(?:com|cn)", s)
# print(new_s)
# arr_s = []
# for str in new_s:
#     arr_s.append(str)
#
# print(arr_s)

# s = "hello world ha ha"
# arr_s = re.split(" ", s)
# print(arr_s)
# print("*"*1000)

# str = lambda x, y: x*y
# print(str(3, 4))

# def fun(*args):
#     for str in args:
#         print(str)
#
# fun("carry","miku","rin")

# def fun(**args):
#     for key in args:
#         print(key + args[key])
#
# fun( name= "carry",age="20")

import urllib.parse
s = "sort=T&range=0,10&tags=%E5%89%A7%E6%83%85,%E7%94%B5%E5%BD%B1"
print(urllib.parse.unquote(s))

