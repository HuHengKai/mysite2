import requests
from lxml import etree
import os

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}


# url="https://www.mzitu.com/"
# response=requests.get(url=url,headers=headers)
# print(response.status_code)
# html=etree.HTML(response.text)
# # url=html.xpath('//ul[@id="pins"]/li/a/@href')
# list=html.xpath('//ul[@id="pins"]/li')
# print(type(url))
# def get_page_url():
#     for i in range(1,212):
#         urls=[]
#         baseurl='https://www.mzitu.com/page/{}'.format(i)
#         response = requests.get(url=baseurl, headers=headers)
#         html = etree.HTML(response.text)
#         lists = html.xpath('//ul[@id="pins"]/li')
#         for list in lists:
#             url=list.xpath("./a/@href")[0]
#             urls.append(url)
#             print(urls)
#     return urls
def get_page_url():
    urls = []
    baseurl = 'https://www.mzitu.com/page/1'
    response = requests.get(url=baseurl, headers=headers)
    html = etree.HTML(response.text)
    lists = html.xpath('//ul[@id="pins"]/li')
    for list in lists:
        url = list.xpath("./a/@href")[0]
        urls.append(url)
        # print(urls)
    print(urls)
    return urls
    # urls = []
    # url = 'https://www.mzitu.com/page/1'
    # response = requests.get(url=url, headers=headers)
    # html = etree.HTML(response.text)
    # lists = html.xpath('//ul[@id="pins"]/li')
    # for list in lists:
    #     url = list.xpath("./a/@href")[0]
    #     urls.append(url)
    #     # print(urls)
    # print(urls)
    # return urls

def download(urls):
    for i in range(len(urls)):
        url=urls[i]
        response = requests.get(url=url, headers=headers)
        html = etree.HTML(response.text)
        max=html.xpath('//div[@class="pagenavi"]/a[5]//text()')
        for i in range(1,max):
            img_url = url + "/{}".format(i)
            print(img_url)



def download_Pic(title, image_list):
    # 新建文件夹
    os.mkdir(title)
    j = 1
    # 下载图片
    for item in image_list:
        filename = '%s/%s.jpg' % (title, str(j))
        print('downloading....%s : NO.%s' % (title, str(j)))
        with open(filename, 'wb') as f:
            img = requests.get(item, headers=headers(item)).content
            f.write(img)
        j += 1





if __name__ == '__main__':
    get_page_url()