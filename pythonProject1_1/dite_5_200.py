import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree
links= ['https://kulturarb.ru/ba/news/220',
'https://kulturarb.ru/ba/news/221',
'https://kulturarb.ru/ba/news/222',
'https://kulturarb.ru/ba/news/223',
'https://kulturarb.ru/ba/news/224',
'https://kulturarb.ru/ba/news/225',
'https://kulturarb.ru/ba/news/226',
'https://kulturarb.ru/ba/news/227',
'https://kulturarb.ru/ba/news/228',
'https://kulturarb.ru/ba/news/229',
'https://kulturarb.ru/ba/news/230',
'https://kulturarb.ru/ba/news/231',
'https://kulturarb.ru/ba/news/232',
'https://kulturarb.ru/ba/news/233',
'https://kulturarb.ru/ba/news/234',
'https://kulturarb.ru/ba/news/235',
'https://kulturarb.ru/ba/news/236',
'https://kulturarb.ru/ba/news/237',
'https://kulturarb.ru/ba/news/238',
'https://kulturarb.ru/ba/news/239',
'https://kulturarb.ru/ba/news/240',
'https://kulturarb.ru/ba/news/241',
'https://kulturarb.ru/ba/news/242',
'https://kulturarb.ru/ba/news/243',
'https://kulturarb.ru/ba/news/244',
'https://kulturarb.ru/ba/news/245',
'https://kulturarb.ru/ba/news/246',
'https://kulturarb.ru/ba/news/247',
'https://kulturarb.ru/ba/news/248',
'https://kulturarb.ru/ba/news/249',
'https://kulturarb.ru/ba/news/250',
'https://kulturarb.ru/ba/news/251',
'https://kulturarb.ru/ba/news/252',
'https://kulturarb.ru/ba/news/253',
'https://kulturarb.ru/ba/news/254',
'https://kulturarb.ru/ba/news/255',
'https://kulturarb.ru/ba/news/256',
'https://kulturarb.ru/ba/news/257',
'https://kulturarb.ru/ba/news/258',
'https://kulturarb.ru/ba/news/259',
'https://kulturarb.ru/ba/news/260',
'https://kulturarb.ru/ba/news/261',
'https://kulturarb.ru/ba/news/262',
'https://kulturarb.ru/ba/news/263']

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
with open(r'result_kulturarb_3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list)
