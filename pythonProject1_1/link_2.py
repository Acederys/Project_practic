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
link_3 = 'https://www.ye02.ru/rss.xml'

def uni_parserd(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    all_item = soup.find_all('item')
    title = []
    content = []
    for k in all_item:
        title.append(k.find('title').text)
        content.append(k.find('turbo:content').text)
    return title, content
content_3 = uni_parserd(link_3)
full_title_3 = content_3[0]
full_content_3 = content_3[1]
