import urllib
import urllib.request as ur

request = ur.Request("http://www.baidu.com")
response = ur.urlopen(request)

print(response.read())