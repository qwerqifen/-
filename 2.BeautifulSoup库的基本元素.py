from bs4 import BeautifulSoup
import requests

url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text  # 服务器返回响应

soup = BeautifulSoup(demo, "html.parser")
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""
print(soup)  # 输出响应的html对象
print('\n')
print(soup.prettify())  # 使用prettify()格式化显示输出
print('\n')


# 获取标签及标签名字name
print(soup.title)  # 获取html的title标签的信息
print(soup.a)  # 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
print(soup.a.name)   # 获取a标签的名字
print(soup.a.parent.name)   # a标签的父标签(上一级标签)的名字
print(soup.a.parent.parent.name)  # a标签的父标签的父标签的名字
print('\n')

# 获取标签的类型及属性attributes
print('a标签类型是：', type(soup.a))   # 查看a标签的类型     类型是啥意思？
print('第一个a标签的属性是：', soup.a.attrs)  # 获取a标签的所有属性(注意到格式是字典)
print('a标签属性的类型是：', type(soup.a.attrs))  # 查看a标签属性的类型
print('a标签的class属性是：', soup.a.attrs['class'])   # 因为是字典，通过字典的方式获取a标签的class属性
print('a标签的href属性是：', soup.a.attrs['href'])   # 同样，通过字典的方式获取a标签的href属性
print('\n')

# 获取标签内非属性字符串NavigableString
print('第一个a标签的内容是：', soup.a.string)  # a标签的非属性字符串信息，表示尖括号之间的那部分字符串
print('a标签的非属性字符串的类型是：', type(soup.a.string))  # 查看标签string字符串的类型
print('第一个p标签的内容是：', soup.p.string)  # p标签的字符串信息(注意p标签中还有个b标签，但是打印string时并未打印b标签，说明string类型是可跨越多个标签层次)

