import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

# все ссылки
# общество
link_1 = 'https://bashgazet.ru/articles/i-tisad'
link_2 = 'https://bashgazet.ru/articles/sport-m-turizm'
link_3 = 'https://bashgazet.ru/articles/ekologiya'
link_4 = 'https://bashgazet.ru/articles/br-normativ-kho-u-i-akttary'
link_5 = 'https://bashgazet.ru/articles/yra-ay-m-khit'
link_6 = 'https://bashgazet.ru/articles/sh-khest-r'
link_7 = 'https://bashgazet.ru/articles/bash-ort-donya-y'
link_8 = 'https://bashgazet.ru/articles/telgen-m-bergen-m'
link_9 = 'https://bashgazet.ru/articles/esh-yuar'
link_10 = 'https://bashgazet.ru/articles/veteran'
link_11 = 'https://bashgazet.ru/articles/m-kh-bb-t-ba-sa-y'
link_12 = 'https://bashgazet.ru/articles/iman'
link_13 = 'https://bashgazet.ru/articles/ba-sa'
link_14 = 'https://bashgazet.ru/articles/t-g-rm-s'
link_15 = 'https://bashgazet.ru/articles/matur-t-en-yaly-y'
link_16 = 'https://bashgazet.ru/articles/ey-ultyra-baly-sy-'
link_17 = 'https://bashgazet.ru/articles/common_material'
link_18 = 'https://bashgazet.ru/articles/g-zitk-ya-ylyu'
link_19 = 'https://bashgazet.ru/articles/yal-s-tend'
link_20 = 'https://bashgazet.ru/articles/kh-ef-e-lek'
link_21 = 'https://bashgazet.ru/articles/intsident'
link_22 = 'https://bashgazet.ru/articles/khaly-i-ben-alyu'
link_23 = 'https://bashgazet.ru/articles/folkloriada'
link_24 = 'https://bashgazet.ru/articles/geroy-ar-d-ere'
link_25 = 'https://bashgazet.ru/articles/novosti'
link_26 = 'https://bashgazet.ru/articles/y-m-i-t'
link_27 = 'https://bashgazet.ru/articles/milli-proekttar'
link_28 = 'https://bashgazet.ru/articles/belem-m-t-rbi'
link_29 = 'https://bashgazet.ru/articles/s-y-s-t-m-kho-u'
link_30 = 'https://bashgazet.ru/articles/-bi-t-m-m-ni-t'
link_31 = 'https://bashgazet.ru/articles/sotsial-m-s-l'
link_32 = 'https://bashgazet.ru/articles/s-l-m-t-bulayy'

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
            full_link = 'https://bashgazet.ru'+item
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
search_link_6 = search_links(link_6)
search_link_7 = search_links(link_7)
search_link_8 = search_links(link_8)
search_link_9 = search_links(link_9)
search_link_10 = search_links(link_10)
search_link_11 = search_links(link_11)
search_link_12 = search_links(link_12)
search_link_13 = search_links(link_13)
search_link_14 = search_links(link_14)
search_link_15 = search_links(link_15)
search_link_16 = search_links(link_16)
search_link_17 = search_links(link_17)
search_link_18 = search_links(link_18)
search_link_19 = search_links(link_19)
search_link_20 = search_links(link_20)
search_link_21 = search_links(link_21)
search_link_22 = search_links(link_22)
search_link_23 = search_links(link_23)
search_link_24 = search_links(link_24)
search_link_25 = search_links(link_25)
search_link_26 = search_links(link_26)
search_link_27 = search_links(link_27)
search_link_28 = search_links(link_28)
search_link_29 = search_links(link_29)
search_link_30 = search_links(link_30)
search_link_31 = search_links(link_31)
search_link_32 = search_links(link_32)



full_body_1 = uni_parserd_ye102(search_link_1)
full_body_2 = uni_parserd_ye102(search_link_2)
full_body_3 = uni_parserd_ye102(search_link_3)
full_body_4 = uni_parserd_ye102(search_link_4)
full_body_5 = uni_parserd_ye102(search_link_5)
full_body_6 = uni_parserd_ye102(search_link_6)
full_body_7 = uni_parserd_ye102(search_link_7)
full_body_8 = uni_parserd_ye102(search_link_8)
full_body_9 = uni_parserd_ye102(search_link_9)
full_body_10 = uni_parserd_ye102(search_link_10)
full_body_11 = uni_parserd_ye102(search_link_11)
full_body_12 = uni_parserd_ye102(search_link_12)
full_body_13 = uni_parserd_ye102(search_link_13)
full_body_14 = uni_parserd_ye102(search_link_14)
full_body_15 = uni_parserd_ye102(search_link_15)
full_body_16 = uni_parserd_ye102(search_link_16)
full_body_17 = uni_parserd_ye102(search_link_17)
full_body_18 = uni_parserd_ye102(search_link_18)
full_body_19 = uni_parserd_ye102(search_link_19)
full_body_20 = uni_parserd_ye102(search_link_20)
full_body_21 = uni_parserd_ye102(search_link_21)
full_body_22 = uni_parserd_ye102(search_link_22)
full_body_23 = uni_parserd_ye102(search_link_23)
full_body_24 = uni_parserd_ye102(search_link_24)
full_body_25 = uni_parserd_ye102(search_link_25)
full_body_26 = uni_parserd_ye102(search_link_26)
full_body_27 = uni_parserd_ye102(search_link_27)
full_body_28 = uni_parserd_ye102(search_link_28)
full_body_29 = uni_parserd_ye102(search_link_29)
full_body_30 = uni_parserd_ye102(search_link_30)
full_body_31 = uni_parserd_ye102(search_link_31)
full_body_32 = uni_parserd_ye102(search_link_32)

full_list = full_body_1 + full_body_2 + full_body_3 + full_body_4 + full_body_5 + full_body_6 + full_body_7 + full_body_8 + full_body_10 + full_body_11 + full_body_12 + full_body_13 + full_body_14 + full_body_15 +full_body_16 + full_body_17 + full_body_18 + full_body_19 + full_body_20 + full_body_21 + full_body_22 + full_body_23 + full_body_24 + full_body_25 +full_body_26 + full_body_27 + full_body_28 + full_body_29 + full_body_30 + full_body_31 + full_body_32

fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
with open(r'result_bashgazet.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list)
