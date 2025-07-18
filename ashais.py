import requests
url='http://www.weather.com.cn/weather1d/101010100.shtml'#爬虫打开的浏览器上的网页
resp=requests.get(url) #打开浏览器并打开网址
# 设置一下编码格式
resp.encoding='utf-8'
print(resp.text)# resp响应对象,对象名.属性名resp.text