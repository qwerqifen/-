import requests
keyword = "python"

try:
    kv = {'wd':keyword}
    r = requests.get("https://www.baidu.com/",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')

#   2443