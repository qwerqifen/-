import requests

def getHTMLText(url):
    try:
        r = requests.get(url) # timeout=30 是干什么的
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return"产生异常"

if __name__== "__main__":
    url = "https://www.baidu.com/"

    r = requests.get(url)
    print(r.status_code)
    print('\n')
    print(getHTMLText(url))


# 一直产生错误 因为requests 不是request