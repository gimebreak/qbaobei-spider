# -*- coding: utf-8 -*-

'''
第二类网页解析工具
'''

def list2str(data,a=[]):
    if isinstance(data,unicode):
        a.append(data)
        return
    for item in data:
        list2str(item,a)
    return ''.join(a)

# 补满url
def add_prefix(response,urls):
    url_parts = response.url.split('/')
    url_parts.pop()
    prefix = '/'.join(url_parts)
    urls = map(lambda url:prefix+url.strip('.'),urls)
    return urls