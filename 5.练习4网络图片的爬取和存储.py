import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "D:\python\python\练习\网络爬虫与信息提取\图片"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):        # os即operating system（操作系统），Python 的 os 模块封装了常见的文件和目录操作
                                        # os.path.exists()就是判断括号里的文件是否存在的意思，括号内的可以是文件路径
        os.mkdir(root)          #在Python中可以使用os.mkdir()函数创建目录（创建一级目录）
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb')as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")


# 一直出错 原因是 path = root + url.split('/')[-1] 写成了 path = root + url.split('\n')[-1] 莫名其妙
