
import requests
from bs4 import BeautifulSoup

r=requests.get('http://python123.io/ws/demo.html')
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify())
print('\n')


# 下行遍历
print(soup.head)
'''
<head><title>This is a python demo page</title></head>
'''
print(soup.head.contents)       #获取head标签的下一层子标签 放在列表里
'''
[<title>This is a python demo page</title>]
'''
print('\n')
print(soup.body.contents,'\n')
print(len(soup.body.contents),'\n')  #输出个数



# 上行遍历
print(soup.title.parent,'\n')
print(soup.html.parent,'\n')
print(soup.parent) # None

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
print('\n')


#平行遍历
print(soup.a.next_sibling,'\n')
print(soup.a.next_sibling.next_sibling,'\n')
print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling) # 空信息