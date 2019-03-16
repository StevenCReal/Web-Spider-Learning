# Web-Spider-Learning
## 一、基础知识
### 1.什么是爬虫？
爬虫，又称网络爬虫(web crawler, web spider)，是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。

### 2.URL
即统一资源定位符，也就是我们说的网址，统一资源定位符是对可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，是互联网上标准资源的地址。互联网上的**每个文件**都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。  
通常URL格式由三部分组成：
- 第一部分是协议(或称为服务方式)。
- 第二部分是存有该资源的主机IP地址(有时也包括端口号)。
- 第三部分是主机资源的具体地址，如目录和文件名等。

### 3.网页是什么？
网页的实质是一段HTML代码，加 JS, CSS。如果把网页比作一个人，那么HTML便是他的骨架，JS便是他的肌肉，CSS便是它的衣服。所以最重要的是HTML

### 4.POST和GET数据传送
数据传送分为POST和GET两种方式，两种方式有什么区别呢？  
最重要的区别是GET方式是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了。
- POST方式： 
```
import urllib
import urllib.request

values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values)  #利用urllib的urlencode方法将字典编码，命名为data
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print(response.read())

```
- GET方式:  
```
import urllib
import urllib.request
 
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data   # 直接把参数写到网址上面，直接构建一个带参数的URL出来即可
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print(response.read())

```
## 二、高级配置用法
### 1.设置Headers
有些网站不会同意程序直接用上面的方式进行访问，如果识别有问题，那么站点根本不会响应，所以为了完全模拟浏览器的工作，我们需要设置一些Headers 的属性。  
```
import urllib  
import urllib2  

url = 'http://www.server.com/login'
# agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
values = {'username' : 'cqc',  'password' : 'XXXX' } 
# 设置headers
headers = { 'User-Agent' : user_agent } 
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() 

```
另外，我们还有对付”反盗链”的方式，对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer。
```
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
          'Referer':'http://www.zhihu.com/articles' } 
```
  
另外还需注意这些Headers的属性：
- User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
- Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
- application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
- application/json ： 在 JSON RPC 调用时使用
- application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
- 在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务

## 三、URL ERROR异常处理
