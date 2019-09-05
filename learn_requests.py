import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

"""
r = requests.get('https://www.douban.com/') # 豆瓣首页
print(r.status_code)
print(r.text)
"""

#对于带参数的URL，传入一个dict作为params参数：
"""

"""
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)#查看编码方式
print(r.content)#用content属性获得bytes对象
"""
"""
