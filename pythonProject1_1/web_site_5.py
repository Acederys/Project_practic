import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

# все ссылки
# общество
link_1 = 'https://kulturarb.ru/ba/news'
link_2 = 'https://kulturarb.ru/ba/news/2'
link_3 = 'https://kulturarb.ru/ba/news/3'
link_4 = 'https://kulturarb.ru/ba/news/4'
link_5 = 'https://kulturarb.ru/ba/news/5'
link_6 = 'https://kulturarb.ru/ba/news/6'


def search_links(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//h4[@class="item-title"]/a/@href')
    return all_links

def uni_parserd_ye102(link):
    full_link_list = []
    new_list=list()
    for item in link:
        if item not in full_link_list:
            full_link = 'https://kulturarb.ru'+item
            full_link_list.append(full_link)
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            if j.find('h1', class_='item-title') is None:
                title ='Na'
            else :
                title = j.find('h1', class_='item-title').text
            if j.find('div', class_='item-text') is None:
                text = 'Na'
            else:
                text = j.find('div', class_='item-text').text
            if j.find('h2', class_='big-lead') is None:
                lead ='Na'
            else:
                lead = j.find('h2', class_='big-lead').text
            if j.find('div', class_='element element-itemcreated first last') is None:
                data = 'Na'
            else:
                data = j.find('div', class_='element element-itemcreated first last').text
            if j.find('a', class_='cm-rubric nuxt-link-active') is None:
                category = 'Яңылыҡтар'
            else:
                category = j.find('a', class_='cm-rubric nuxt-link-active')
            if j.find('div', class_='tags') is None:
                tags = 'Na'
            else:
                tags = j.find('div', class_='tags').text
            dict_content = {
                'url': elem,
                'title': title,
                'lead': lead,
                'content': text,
                'data': data,
                'category': category,
                'tags': tags
            }

            new_list.append(dict_content)
    return new_list

search_link_1 = search_links(link_1)
search_link_2 = search_links(link_2)
search_link_3 = search_links(link_3)
search_link_4 = search_links(link_4)
search_link_5 = search_links(link_5)
search_link_6 = search_links(link_6)

full_body_1 = uni_parserd_ye102(search_link_1)
full_body_2 = uni_parserd_ye102(search_link_2)
full_body_3 = uni_parserd_ye102(search_link_3)
full_body_4 = uni_parserd_ye102(search_link_4)
full_body_5 = uni_parserd_ye102(search_link_5)
full_body_6 = uni_parserd_ye102(search_link_6)


full_list = full_body_1 + full_body_2 + full_body_3 +full_body_4 + full_body_5 + full_body_6

fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
with open(r'result_kulturarb.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list)
