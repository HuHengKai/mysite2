# encoding = utf-8
import concurrent
import os
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
from lxml import etree


def header(referer):

    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        # 'Referer': '{}'.format(referer),
    }

    return headers


def request_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def get_page_urls():
    urls = []
    baseurl = 'https://www.mzitu.com/page/1'
    response = requests.get(url=baseurl)
    html = etree.HTML(response.text)
    lists = html.xpath('//ul[@id="pins"]/li')
    for list in lists:
        url = list.xpath("./a/@href")[0]
        urls.append(url)
        print("*"*10)
    print(urls)
    return urls


# def download_Pic(title, image_list):
#     # 新建文件夹
#     os.mkdir(title)
#     j = 1
#     # 下载图片
#     for item in image_list:
#         filename = '%s/%s.jpg' % (title, str(j))
#         print('downloading....%s : NO.%s' % (title, str(j)))
#         with open(filename, 'wb') as f:
#             img = requests.get(item, headers=header(item)).content
#             f.write(img)
#         j += 1

def download(url):
    html = request_page(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string
    title = soup.find('h2').string
    image_list = []

    for i in range(int(total)):
        html = request_page(url + '/%s' % (i + 1))
        soup = BeautifulSoup(html, 'lxml')
        img_url = soup.find('img').get('src')
        print(img_url)
        image_list.append(img_url)

    # download_Pic(title, image_list)



def download_all_images(list_page_urls):
    # 获取每一个详情妹纸
    works = len(list_page_urls)
    with concurrent.futures.ThreadPoolExecutor(works) as exector:
        for url in list_page_urls:
            exector.submit(download,url)

if __name__ == '__main__':
    # 获取每一页的链接和名称
    get_page_urls()
    # list_page_urls = get_page_urls()
    # download_all_images(list_page_urls)