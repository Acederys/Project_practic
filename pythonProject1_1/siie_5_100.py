import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree
links = ['https://kulturarb.ru/ba/news/115',
'https://kulturarb.ru/ba/news/116',
'https://kulturarb.ru/ba/news/117',
'https://kulturarb.ru/ba/news/118',
'https://kulturarb.ru/ba/news/119',
'https://kulturarb.ru/ba/news/120',
'https://kulturarb.ru/ba/news/121',
'https://kulturarb.ru/ba/news/122',
'https://kulturarb.ru/ba/news/123',
'https://kulturarb.ru/ba/news/124',
'https://kulturarb.ru/ba/news/125',
'https://kulturarb.ru/ba/news/126',
'https://kulturarb.ru/ba/news/127',
'https://kulturarb.ru/ba/news/128',
'https://kulturarb.ru/ba/news/129',
'https://kulturarb.ru/ba/news/130',
'https://kulturarb.ru/ba/news/131',
'https://kulturarb.ru/ba/news/132',
'https://kulturarb.ru/ba/news/133',
'https://kulturarb.ru/ba/news/134',
'https://kulturarb.ru/ba/news/135',
'https://kulturarb.ru/ba/news/136',
'https://kulturarb.ru/ba/news/137',
'https://kulturarb.ru/ba/news/138',
'https://kulturarb.ru/ba/news/139',
'https://kulturarb.ru/ba/news/140',
'https://kulturarb.ru/ba/news/141',
'https://kulturarb.ru/ba/news/142',
'https://kulturarb.ru/ba/news/143',
'https://kulturarb.ru/ba/news/144',
'https://kulturarb.ru/ba/news/145',
'https://kulturarb.ru/ba/news/146',
'https://kulturarb.ru/ba/news/147',
'https://kulturarb.ru/ba/news/148',
'https://kulturarb.ru/ba/news/149',
'https://kulturarb.ru/ba/news/150',
'https://kulturarb.ru/ba/news/151',
'https://kulturarb.ru/ba/news/152',
'https://kulturarb.ru/ba/news/153',
'https://kulturarb.ru/ba/news/154',
'https://kulturarb.ru/ba/news/155',
'https://kulturarb.ru/ba/news/156',
'https://kulturarb.ru/ba/news/157',
'https://kulturarb.ru/ba/news/158',
'https://kulturarb.ru/ba/news/159',
'https://kulturarb.ru/ba/news/160',
'https://kulturarb.ru/ba/news/161',
'https://kulturarb.ru/ba/news/162',
'https://kulturarb.ru/ba/news/163',
'https://kulturarb.ru/ba/news/164',
'https://kulturarb.ru/ba/news/165',
'https://kulturarb.ru/ba/news/166',
'https://kulturarb.ru/ba/news/167',
'https://kulturarb.ru/ba/news/168',
'https://kulturarb.ru/ba/news/169',
'https://kulturarb.ru/ba/news/170',
'https://kulturarb.ru/ba/news/171',
'https://kulturarb.ru/ba/news/172',
'https://kulturarb.ru/ba/news/173',
'https://kulturarb.ru/ba/news/174',
'https://kulturarb.ru/ba/news/175',
'https://kulturarb.ru/ba/news/176',
'https://kulturarb.ru/ba/news/177',
'https://kulturarb.ru/ba/news/178',
'https://kulturarb.ru/ba/news/179',
'https://kulturarb.ru/ba/news/180',
'https://kulturarb.ru/ba/news/181',
'https://kulturarb.ru/ba/news/182',
'https://kulturarb.ru/ba/news/183',
'https://kulturarb.ru/ba/news/184',
'https://kulturarb.ru/ba/news/185',
'https://kulturarb.ru/ba/news/186',
'https://kulturarb.ru/ba/news/187',
'https://kulturarb.ru/ba/news/188',
'https://kulturarb.ru/ba/news/189',
'https://kulturarb.ru/ba/news/190'
'https://kulturarb.ru/ba/news/191',
'https://kulturarb.ru/ba/news/192',
'https://kulturarb.ru/ba/news/193',
'https://kulturarb.ru/ba/news/194',
'https://kulturarb.ru/ba/news/195',
'https://kulturarb.ru/ba/news/196',
'https://kulturarb.ru/ba/news/197',
'https://kulturarb.ru/ba/news/198',
'https://kulturarb.ru/ba/news/199',
'https://kulturarb.ru/ba/news/200',
'https://kulturarb.ru/ba/news/201',
'https://kulturarb.ru/ba/news/202',
'https://kulturarb.ru/ba/news/203',
'https://kulturarb.ru/ba/news/204',
'https://kulturarb.ru/ba/news/205',
'https://kulturarb.ru/ba/news/206',
'https://kulturarb.ru/ba/news/207',
'https://kulturarb.ru/ba/news/208',
'https://kulturarb.ru/ba/news/209',
'https://kulturarb.ru/ba/news/210',
'https://kulturarb.ru/ba/news/211',
'https://kulturarb.ru/ba/news/212',
'https://kulturarb.ru/ba/news/213',
'https://kulturarb.ru/ba/news/214',
'https://kulturarb.ru/ba/news/215',
'https://kulturarb.ru/ba/news/216',
'https://kulturarb.ru/ba/news/217',
'https://kulturarb.ru/ba/news/218',
'https://kulturarb.ru/ba/news/219']

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
    search_links = search_links(url)
    for item in search_links:
        full_body = uni_parserd_ye102(item)
        full_list.append(full_body)


fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
with open(r'result_kulturarb_2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list)
