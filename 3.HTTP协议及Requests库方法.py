import requests

# 一 .Requests库的put()方法、
payload = {'key1':'value1','key2':'value2'}
r = requests.put('http://httpbin.org/put',data = payload)
print(r.text)
print('\n')
# 字典默认放在form

'''
{
  ...
  "form": {
    "key1": "value1", 
    "key2": "value2"
  ...
  }, 
 '''

# 二.Requests库的post()方法
r = requests.post('http://httpbin.org/post',data='ABC')
print(r.text)
print('\n')
'''
 "data": "ABC",         向url post一个字符串 自动编码为data
'''

payload = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data = payload)
print(r.text)
print('\n')
'''
 "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  
  向url post一个字典 自动编码位form
'''

# Requests库的head()方法
r = requests.head('http://httpbin.org/get')
print(r.headers)
print('\n')
print(r.text)
