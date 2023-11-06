import requests
from bs4 import BeautifulSoup
import csv
# import pandas as pd
from lxml import etree

# все ссылки
links = ['https://bash.bashinform.ru/news/social']


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
            full_link = 'https://bash.bashinform.ru'+item
            full_link_list.append(full_link)
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            if j.find('h1', class_='h1') is None:
                title ='Na'
            else :
                title = j.find('h1', class_='h1').text
            if j.find('div', class_='paragraph serif-text') is None:
                text = 'Na'
            else:
                text = j.find('div', class_='paragraph serif-text').text
            if j.find('h2', class_='big-lead') is None:
                lead ='Na'
            else:
                lead = j.find('h2', class_='big-lead').text
            if j.find('div', class_='cm-date') is None:
                data = 'Na'
            else:
                data = j.find('div', class_='cm-date').text
            if j.find('a', class_='cm-rubric nuxt-link-active') is None:
                category = 'Na'
            else:
                category = j.find('a', class_='cm-rubric nuxt-link-active').text
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
    print(item)
# fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
# with open(r'result_bash.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(full_list)
