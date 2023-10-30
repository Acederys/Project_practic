import requests
from bs4 import BeautifulSoup
import csv
# import pandas as pd
from lxml import etree

# все ссылки
link_1 = 'https://bash.bashinform.ru/news/social'
link_2 = 'https://bash.bashinform.ru/news/sport'
link_3 = 'https://bash.bashinform.ru/news/economy'
link_4 = 'https://bash.bashinform.ru/news/law'
link_5 = 'https://bash.bashinform.ru/news/culture'
link_7 = 'https://bash.bashinform.ru/news/politics'



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

search_link_1 = search_links(link_1)
search_link_2 = search_links(link_2)
search_link_3 = search_links(link_3)
search_link_4 = search_links(link_4)
search_link_5 = search_links(link_5)
search_link_7 = search_links(link_7)


full_body_1 = uni_parserd_ye102(search_link_1)
full_body_2 = uni_parserd_ye102(search_link_2)
full_body_3 = uni_parserd_ye102(search_link_3)
full_body_4 = uni_parserd_ye102(search_link_4)
full_body_5 = uni_parserd_ye102(search_link_5)
full_body_7 = uni_parserd_ye102(search_link_7)


full_list = full_body_1 + full_body_2 + full_body_3 + full_body_4 + full_body_5 + full_body_7

fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
with open(r'result_bash.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list)
