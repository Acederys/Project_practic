import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree
links = ['https://kulturarb.ru/ba/news/51',
'https://kulturarb.ru/ba/news/52',
'https://kulturarb.ru/ba/news/53',
'https://kulturarb.ru/ba/news/54',
'https://kulturarb.ru/ba/news/55',
'https://kulturarb.ru/ba/news/56',
'https://kulturarb.ru/ba/news/57',
'https://kulturarb.ru/ba/news/58',
'https://kulturarb.ru/ba/news/59',
'https://kulturarb.ru/ba/news/60',
'https://kulturarb.ru/ba/news/61',
'https://kulturarb.ru/ba/news/62',
'https://kulturarb.ru/ba/news/63',
'https://kulturarb.ru/ba/news/64',
'https://kulturarb.ru/ba/news/65',
'https://kulturarb.ru/ba/news/66',
'https://kulturarb.ru/ba/news/67',
'https://kulturarb.ru/ba/news/68',
'https://kulturarb.ru/ba/news/69',
'https://kulturarb.ru/ba/news/70',
'https://kulturarb.ru/ba/news/71',
'https://kulturarb.ru/ba/news/72',
'https://kulturarb.ru/ba/news/73',
'https://kulturarb.ru/ba/news/74',
'https://kulturarb.ru/ba/news/75',
'https://kulturarb.ru/ba/news/76',
'https://kulturarb.ru/ba/news/77',
'https://kulturarb.ru/ba/news/78',
'https://kulturarb.ru/ba/news/79',
'https://kulturarb.ru/ba/news/80',
'https://kulturarb.ru/ba/news/81',
'https://kulturarb.ru/ba/news/82',
'https://kulturarb.ru/ba/news/83',
'https://kulturarb.ru/ba/news/84',
'https://kulturarb.ru/ba/news/85',
'https://kulturarb.ru/ba/news/86',
'https://kulturarb.ru/ba/news/87',
'https://kulturarb.ru/ba/news/88',
'https://kulturarb.ru/ba/news/89',
'https://kulturarb.ru/ba/news/90'
'https://kulturarb.ru/ba/news/91',
'https://kulturarb.ru/ba/news/92',
'https://kulturarb.ru/ba/news/93',
'https://kulturarb.ru/ba/news/94',
'https://kulturarb.ru/ba/news/95',
'https://kulturarb.ru/ba/news/96',
'https://kulturarb.ru/ba/news/97',
'https://kulturarb.ru/ba/news/98',
'https://kulturarb.ru/ba/news/99',
'https://kulturarb.ru/ba/news/100',
'https://kulturarb.ru/ba/news/101',
'https://kulturarb.ru/ba/news/102',
'https://kulturarb.ru/ba/news/103',
'https://kulturarb.ru/ba/news/104',
'https://kulturarb.ru/ba/news/105',
'https://kulturarb.ru/ba/news/106',
'https://kulturarb.ru/ba/news/107',
'https://kulturarb.ru/ba/news/108',
'https://kulturarb.ru/ba/news/109',
'https://kulturarb.ru/ba/news/110',
'https://kulturarb.ru/ba/news/111',
'https://kulturarb.ru/ba/news/112',
'https://kulturarb.ru/ba/news/113',
'https://kulturarb.ru/ba/news/114']

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
full_list = list()
for url in links:
    search_link = search_links(url)
    full_body = uni_parserd_ye102(search_link)
    full_list.append(full_body)

for item in full_list:
    fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
    with open(r'result_kulturarb_1.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(item)
