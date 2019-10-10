import requests

r = requests.get("https://www.tencent.com")
print(r.status_code)    #HTTP请求返回的状态，200表示连接成功，404表示连接失败
print('\n')
print(r.text)       #网页内容的字符串形式
print('\n')
print(r.encoding)       #从HTTP HEARD 中猜测的相应内容的编码形式
print('\n')
print(r.apparent_encoding)      #从内容中分析出响应内容的编码形式
print('\n')
r.encoding = 'utf-8' #可以显示中文的编码
print(r.text)
print('\n')