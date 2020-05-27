'''
用urllib链接，获取网页内容，并提取链接
'''
from urllib.request import urlopen
import re
# from bs4 import BeautifulSoup

html = urlopen(
    'https://morvanzhou.github.io/static/scraping/basic-structure.html'
).read().decode('utf-8')

print(html)

link = re.findall(r'href="(.*)"', html)
print("link=\n"+"%s\n"*len(link) % tuple(i for i in link))
