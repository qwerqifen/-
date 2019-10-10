import requests
r = requests.get("https://python123.io/ws/demo.html")
print(r.text)
print('\n')
demo = r.text


from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser") # html.parser HTML进行解析,提取HTML的数据或者修改HTML数据,
print(soup.prettify())      # soup.prettify() 使解析出来的html程序“每逢标签，自动换行”
