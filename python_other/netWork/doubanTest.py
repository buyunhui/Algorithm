import urllib.request
"""
��ʱ����ˮ
"""
data = bytes(urllib.parse.urlencode({'name':'zhangsan'}),encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())