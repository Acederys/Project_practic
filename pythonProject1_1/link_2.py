import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree
# # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#
# # для сайта https://forum-zauralye.com/ba/news/
#
# link_3 = 'https://forum-zauralye.com/ba/news/'
#
# # создали список ссылок на статьи
# def search_links_2(link):
#     url = requests.get(link)
#
#     soup = BeautifulSoup(url.content, 'html.parser')
#     dom = etree.HTML(str(soup))
#     all_links = dom.xpath('//*[@class="item"]/a/@href')
#
#     return all_links
# full_link_list = []
# def uni_parserd_2(link):
#     for item in link:
#         if item not in full_link_list:
#             full_link = 'https://forum-zauralye.com'+item
#             full_link_list.append(full_link)
#     title = []
#     content = []
#     for elem in full_link_list:
#         url = requests.get(elem)
#         soup = BeautifulSoup(url.content, 'html.parser')
#         all_content = soup.find_all('body')
#         for j in all_content:
#             title.append(j.find('h1', class_='item-title').text)
#             content.append(j.find('div', class_='item-text').text)
#     return title, content
#
# search_link = search_links_2(link_3)
# full_content = uni_parserd_2(search_link)
#
# title_dict = full_content[0]
# content_dict = full_content[1]
# print(len(title_dict))
# print(len(content_dict))
# # all_dict = {'Title': title_dict, 'Content': content_dict}
# #
# # content_frame = pd.DataFrame(all_dict)
# #
# # content_frame.to_csv (r' result.csv', index= False )
# для сайта https://bashgazet.ru/articles/milli-proekttar Национальные проекты


# link_7 = 'https://bashgazet.ru/articles/milli-proekttar'
#
# # создали список ссылок на статьи
# def search_links_7(link):
#     url = requests.get(link)
#
#     soup = BeautifulSoup(url.content, 'html.parser')
#     dom = etree.HTML(str(soup))
#     all_links = dom.xpath('//a[@class="item item"]/@href')
#     return all_links
#
# full_link_list_7 = []
# def uni_parserd_7(link):
#     for item in link:
#         if item not in full_link_list_7:
#             full_link = 'https://bashgazet.ru'+item
#             full_link_list_7.append(full_link)
#     print(full_link_list_5)
    # title = []
#     content = []
#     for elem in full_link_list_7:
#         url = requests.get(elem)
#         soup = BeautifulSoup(url.content, 'html.parser')
#         all_content = soup.find_all('body')
#         for j in all_content:
#             title.append(j.find('h1', class_='h1').text)
#             content.append(j.find('div', class_='paragraph serif-text').text)
#     return title, content
# #
# search_link_7 = search_links_7(link_7)
# full_content_7 = uni_parserd_7(search_link_7)
#
# full_title_7 = full_content_7[0]
# full_content_7 = full_content_7[1]
#
# print(len(full_title_7))
# print(len(full_content_7))
# для сайта https://gulshat1.ucoz.net/news/rss/ ВСЕ КАТЕГОРИИ


# link_4 = 'https://misrbash.moy.su/news/rss/'
#
# def uni_parserd_4(link):
#     url = requests.get(link)
#     soup = BeautifulSoup(url.content, 'xml')
#     all_item = soup.find_all('item')
#     title = []
#     content = []
#     for k in all_item:
#         title.append(k.find('title').text)
#         content.append(k.find('content:encoded').text)
#     return title, content
#
# def search_cat_4(link):
#     url = requests.get(link)
#     soup = BeautifulSoup(url.content, 'xml')
#     all_category = soup.find_all('item')
#     print(all_category)
#     cat_list = []
#     for g in all_category:
#         cat_list.append(g.find('category').text)
#         print(cat_list)
#
# content_4 = uni_parserd_4(link_4)
# full_title_4 = content_4[0]
# full_content_4 = content_4[1]
# list_category_4 = search_cat_4(link_4)


link_4 = 'https://ye102.ru/articles/pl'
def search_links_1(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

def uni_parserd_1(link):
    full_link_list_1 = []
    for item in link:
        if item not in full_link_list_1:
            full_link = 'https://ye102.ru'+item
            full_link_list_1.append(full_link)
    title = []
    content = []
    for elem in full_link_list_1:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        print(all_content)
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text'))
    print(title, content)

def search_cat_8(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Сәйәсәт һәм хоҡуҡ')
    return catgory_2
search_link_4 = search_links_1(link_4)
full_body_4 = uni_parserd_1(search_link_4)

full_title_4 = full_body_4[0]
full_content_4 = full_body_4[1]
list_cat_4 = search_cat_8(full_title_4)
