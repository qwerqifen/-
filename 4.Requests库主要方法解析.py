# request库主要用get head

import requests

'''
fs = {'file':open('data.xls','rb')}
r = requests.request('POST','http://python123.io/ws',file=fs)
        显示无data.xls
'''



kv = {'key1':'value1'}
r = requests.get("http://python123.io/ws")
print(r.text)
print('\n')



kv = {'key1':'value1','key2':'value2'}
r = requests.request('GET','http://python123.io/ws',params=kv)
print(r.url)
# https://python123.io/ws?key1=value1&key2=value2


r = requests.get('https://www.baidu.com/')
e = requests.head('https://www.baidu.com/')
print(e.text)
print('\n')
print(r.text)

