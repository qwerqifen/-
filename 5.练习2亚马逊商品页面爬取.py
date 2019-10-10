import requests

r = requests.get("https://www.amazon.cn/dp/B07RB134KX?_encoding=UTF8&ref_=pc_cxrd_116169071_bestTab_116169071_a_best_1&pf_rd_p=ffd15da5-81b5-4e18-891c-3e8e740d5cc4&pf_rd_s=merchandised-search-3&pf_rd_t=101&pf_rd_i=116169071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=8X9V86J4W450YJH8JVH7&pf_rd_r=8X9V86J4W450YJH8JVH7&pf_rd_p=ffd15da5-81b5-4e18-891c-3e8e740d5cc4")
print(r.status_code)
print(r.encoding)
print(r.request.headers)


kv = {'user-agent':'Mozilla/5.0'}
url = "https://www.amazon.cn/dp/B07RB134KX?_encoding=UTF8&ref_=pc_cxrd_116169071_bestTab_116169071_a_best_1&pf_rd_p=ffd15da5-81b5-4e18-891c-3e8e740d5cc4&pf_rd_s=merchandised-search-3&pf_rd_t=101&pf_rd_i=116169071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=8X9V86J4W450YJH8JVH7&pf_rd_r=8X9V86J4W450YJH8JVH7&pf_rd_p=ffd15da5-81b5-4e18-891c-3e8e740d5cc4"
r = requests.get(url,headers=kv)
print(r.request.headers)
print(r.status_code)
print('\n')


try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')
