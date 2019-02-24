import re

# pattern = "carry"
# str = "carry"
# result = re.match(pattern, str)
# print(result)
#
# help(result)

#print(re.match("\d", "2"))
#print(re.match(".\d", "a1"))
#print(re.match("\D", "a"))
#print(re.match("\s", " "))
#print(re.match("\S", "aaa"))
#print(re.match("\w", "a"))
#print(re.match("[a-z3-5]", "s"))
#print(re.match(" ", " a"))
#print(re.match("\d{2}", "123456"))
#print(re.match("1[35678]\d{9}$", "18379727052"))
#print(r"\\")
#print(re.match("[A-Z][a-z]*", "A"))
#print(re.match("[a-zA-Z_]+\w", "_name"))
#print(re.match("[0-9]?[0-9]", "22"))
#print(re.match("\w{2,3}", "wwwww"))
#print(re.match("\w{4,20}@163\.com$", "hello@163.com"))
# print(re.match(r"\d*", "1234"))
# print("\n")

# print(re.match(r"(jpg|png).", "jpga"))

#print(re.match("([^-]*)-(\d+)", "010-12345678"

s = '''
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
# '''
# result = re.sub(r"</?\w+?>", "", s)
# print(result)

s = "http://c1.piapro.jp/timg/vr1ngz6pngyxmxye_20180126195230_0740_0500.pngaaaahttp://c1.piapro.jp/timg/vr1ngz6pngyxmxye_20180126195230_0740_0500.png"
result  = re.findall(r"http://c1.+(?:png|jpg|jpeg)", s)
print(result)

# s = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">请提取url地址'
# result = re.findall("https.+?\.jpg", s)
# print(result)

# ret = re.match("\w{4}(163|126|qq)\.com", "test163.com")
# print(ret)

# s = r"https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E6%9D%8E%E6%98%93%E5%B3%B0&step_word=&hs=0&pn=3&spn=0&di=55949737360&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=undefined&lm=undefined&st=undefined&cs=3132249016%2C3245953538&os=3854204130%2C3544894708&simid=4154354610%2C635562303&adpicid=0&lpn=0&ln=3942&fr=&fmq=1516968654194_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=star&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg4q.duitang.com%2Fuploads%2Fitem%2F201503%2F21%2F20150321171207_EX4ae.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B17tpwg2_z%26e3Bv54AzdH3Frj5rsjAzdH3F4ks52AzdH3Fnmdncn9abAzdH3F1jpwtsAzdH3F&gsm=0&rpstart=0&rpnum=0.jpgjpg"
# pattern = "https.*?jpg"
# result = re.findall(pattern, s)
# print(result)

# ret = re.findall("\.(jpg|png)", "http://.png")
# print(ret)

# s="http://c1.piapro.jp/timg/vr1ngz6pngyxmxye_20180126195230_0740_0500.jpg"
# # pattern = "http.*?jpg"
# pattern = "(http:[^\s]*?(jpg|png|PNG|JPG))"
# result = re.findall(pattern, s)
# print(result)

# for i in range(1,2):
#     print(i)


# s = "sssafsaf.jpg"
# s = s[-3:]
# print(s)
if not "":
    print("aaa")

