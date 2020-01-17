import requests
from bs4 import BeautifulSoup
import xlwt
from lxml import etree

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}



book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')

n = 1

url='https://movie.douban.com/top250?start=0&filter='
respnsonse = requests.get(url,headers=headers)
print(respnsonse.status_code)
html=etree.HTML(respnsonse.text)

list=html.xpath('//ol[@class="grid_view"]/li')

for li in list:
    item_name =li.xpath('.//span[@class="title"][1]/text()')
    # print(item_name)
    item_img =li.xpath('.//img/@src')
    item_index = li.xpath('.//em/text()')
    item_score = li.xpath('.//span[@class="rating_num"]/text()')
    item_author = li.xpath('.//span[@class="title"][2]/text()[1]')

    if (li.xpath('.//span[@class="inq"]/text()')!= None):
        item_intr =li.xpath('.//span[@class="inq"]/text()')

    # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
    # print('爬取电影：', item_name,item_index,item_intr,item_score)
    print(item_author)
    n

    sheet.write(n, 0, item_name)
    sheet.write(n, 1, item_img)
    sheet.write(n, 2, item_index)
    sheet.write(n, 3, item_score)
    sheet.write(n, 4, item_author)
    sheet.write(n, 5, item_intr)

    n = n + 1
