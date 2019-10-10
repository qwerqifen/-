# 对不齐 烦死了！

'''

步骤1：getHTMLText()  从网络上获取大学排名网页内容

步骤2：fillUnivList()    提取网页内容中信息到合适的数据结构

步骤3：printUnivList()   利用数据结构展示并输出结果
'''
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag): # 过滤掉非标签字符串
            tds = tr('td') # 将tr中的所有td标签(一共四个)存入tds列表中
            ulist.append([tds[0].string, tds[1].string, tds[3].string]) #分别对应 （排名    学校名称　　总分）

def printUnivList(ulist, num):
    tplt = "{0:{3}^10}\t{1:{3}^12}\t{2:{3}^15}" #\t空格
    print(tplt.format("排名", "学校名称", "总分", chr(12288))) #chr(12288)采用中文字符的空格填充
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288))) #{0:^10}\t{1:{3}^12}\t{2:^10}，0.1.2对应u[0], u[1], u[2]，
                                                            #但是^10  {3}^12是什么意思？


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs


main()

