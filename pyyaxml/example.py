# -*- coding: utf-8 -*-
import sys

from pyyaxml.search import YaSearch


# Put your Yandex.XML credentials here 
API_USER = ''
API_KEY = ''

y = YaSearch(API_USER, API_KEY,'com')
results = y.search('ricardo')
print(results.error.description)
for i in results.items:
    print(i.url)
    print(i.title)

