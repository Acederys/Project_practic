import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

# все ссылки
# общество
link_1 = 'https://ye102.ru/articles/obschestvo'
# link_2 = 'https://ye102.ru/articles/pl'
# экономика
link_3 = 'https://ye102.ru/articles/ek'
# link_4 = 'https://ye102.ru/articles/litra'
link_5 = 'https://ye102.ru/articles/konkurs'
link_6 = 'https://ye102.ru/articles/obrazovanie'
link_7 = 'https://ye102.ru/articles/ht'
link_8 = 'https://ye102.ru/articles/zd'
# link_9 = 'https://ye102.ru/articles/iman'
link_10 = 'https://ye102.ru/articles/pd'
link_11 = 'https://ye102.ru/articles/mahsus'
# спорт
link_12 = 'https://ye102.ru/articles/sport'
link_13 = 'https://ye102.ru/articles/guzel'
link_14 = 'https://ye102.ru/articles/novosti'
link_15 = 'https://ye102.ru/articles/ya-yly-tar-ta-ma-y-netu'


def search_links(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

def uni_parserd_ye102(link):
    full_link_list = []
    new_list=list()
    for item in link:
        if item not in full_link_list:
            full_link = 'https://ye102.ru'+item
            full_link_list.append(full_link)
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            dict_content = {
                'url': elem,
                'title': j.find('h1', class_='h1').text,
                'content': j.find('div', class_='paragraph serif-text').text + ' ' + j.find('h2', class_='big-lead').text,
                'data': j.find('div', class_='cm-date').text,
                'category': j.find('a', class_='cm-rubric nuxt-link-active').text
            }
            new_list.append(dict_content)
    return new_list

search_link_1 = search_links(link_1)
# search_link_2 = search_links(link_2)
search_link_3 = search_links(link_3)
# search_link_4 = search_links(link_4)
search_link_5 = search_links(link_5)
search_link_6 = search_links(link_6)
search_link_7 = search_links(link_7)
search_link_8 = search_links(link_8)
# search_link_9 = search_links(link_9)
search_link_10 = search_links(link_10)
search_link_11 = search_links(link_11)
search_link_12 = search_links(link_12)
search_link_13 = search_links(link_13)
search_link_14 = search_links(link_14)
search_link_15 = search_links(link_15)

full_body_1 = uni_parserd_ye102(search_link_1)
# full_body_2 = uni_parserd_ye102(search_link_2)
full_body_3 = uni_parserd_ye102(search_link_3)
# full_body_4 = uni_parserd_ye102(search_link_4)
full_body_5 = uni_parserd_ye102(search_link_5)
full_body_6 = uni_parserd_ye102(search_link_6)
full_body_7 = uni_parserd_ye102(search_link_7)
full_body_8 = uni_parserd_ye102(search_link_8)
# full_body_9 = uni_parserd_ye102(search_link_9)
full_body_10 = uni_parserd_ye102(search_link_10)
full_body_11 = uni_parserd_ye102(search_link_11)
full_body_12 = uni_parserd_ye102(search_link_12)
full_body_13 = uni_parserd_ye102(search_link_13)
full_body_14 = uni_parserd_ye102(search_link_14)
full_body_15 = uni_parserd_ye102(search_link_15)

full_list = full_body_1 + full_body_3 + full_body_5 + full_body_6 + full_body_7 + full_body_8 + full_body_10 + full_body_11 + full_body_12 + full_body_13 + full_body_14 + full_body_15
# print(full_list)
# with open(r'result_ye102.csv','w', encoding='utf-8', newline='') as results:
#     writer = csv.writer(results, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     for item in full_list:
#         writer.writerow(item.values())
# csv header
fieldnames = ['url', 'title', 'content', 'data', 'category']
with open(r'result_ye102.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list)
