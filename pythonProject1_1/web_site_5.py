import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

# все ссылки
# общество
links_1 = 'https://kulturarb.ru/ba/news/191'
links_2 = 'https://kulturarb.ru/ba/news/192'
links_3 = 'https://kulturarb.ru/ba/news/193'
links_4 = 'https://kulturarb.ru/ba/news/194'
links_5 = 'https://kulturarb.ru/ba/news/195'
links_6 = 'https://kulturarb.ru/ba/news/196'
links_7 = 'https://kulturarb.ru/ba/news/197'
links_8 = 'https://kulturarb.ru/ba/news/198'
links_9 = 'https://kulturarb.ru/ba/news/199'
links_10 = 'https://kulturarb.ru/ba/news/200'
links_11 = 'https://kulturarb.ru/ba/news/201'
links_12 = 'https://kulturarb.ru/ba/news/202'
links_13 = 'https://kulturarb.ru/ba/news/203'
links_14 = 'https://kulturarb.ru/ba/news/204'
links_15 = 'https://kulturarb.ru/ba/news/205'
links_16= 'https://kulturarb.ru/ba/news/206'
links_17 = 'https://kulturarb.ru/ba/news/207'
links_18 = 'https://kulturarb.ru/ba/news/208'
links_19 = 'https://kulturarb.ru/ba/news/209'
links_20 = 'https://kulturarb.ru/ba/news/210'
links_21 = 'https://kulturarb.ru/ba/news/211'
links_22 = 'https://kulturarb.ru/ba/news/212'
links_23 = 'https://kulturarb.ru/ba/news/213'
links_24 = 'https://kulturarb.ru/ba/news/214'
links_25 = 'https://kulturarb.ru/ba/news/215'
links_26 = 'https://kulturarb.ru/ba/news/216'
links_27 = 'https://kulturarb.ru/ba/news/217'
links_28 = 'https://kulturarb.ru/ba/news/218'
links_29 = 'https://kulturarb.ru/ba/news/219'
links_30 = 'https://kulturarb.ru/ba/news/220'
links_31 = 'https://kulturarb.ru/ba/news/221'
links_32 = 'https://kulturarb.ru/ba/news/222'
links_33 = 'https://kulturarb.ru/ba/news/223'
links_34 = 'https://kulturarb.ru/ba/news/224'
links_35 = 'https://kulturarb.ru/ba/news/225'
links_36 = 'https://kulturarb.ru/ba/news/226'
links_37 = 'https://kulturarb.ru/ba/news/227'
links_38 = 'https://kulturarb.ru/ba/news/228'
links_39 = 'https://kulturarb.ru/ba/news/229'
links_40 = 'https://kulturarb.ru/ba/news/230'
links_41 = 'https://kulturarb.ru/ba/news/231'
links_42 = 'https://kulturarb.ru/ba/news/232'
links_43 = 'https://kulturarb.ru/ba/news/233'
links_44 = 'https://kulturarb.ru/ba/news/234'
links_45 = 'https://kulturarb.ru/ba/news/235'
links_46 = 'https://kulturarb.ru/ba/news/236'
links_47 = 'https://kulturarb.ru/ba/news/237'
links_48 = 'https://kulturarb.ru/ba/news/238'
links_49 = 'https://kulturarb.ru/ba/news/239'
links_50 = 'https://kulturarb.ru/ba/news/240'



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
search_link_1 = search_links(links_1)
search_link_2 = search_links(links_2)
search_link_3 = search_links(links_3)
search_link_4 = search_links(links_4)
search_link_5 = search_links(links_5)
search_link_6 = search_links(links_6)
search_link_7 = search_links(links_7)
search_link_8 = search_links(links_8)
search_link_9 = search_links(links_9)
search_link_10 = search_links(links_10)
search_link_11 = search_links(links_11)
search_link_12 = search_links(links_12)
search_link_13 = search_links(links_13)
search_link_14 = search_links(links_14)
search_link_15 = search_links(links_15)
search_link_16 = search_links(links_16)
search_link_17 = search_links(links_17)
search_link_18 = search_links(links_18)
search_link_19 = search_links(links_19)
search_link_20 = search_links(links_20)
search_link_21 = search_links(links_21)
search_link_22 = search_links(links_22)
search_link_23 = search_links(links_23)
search_link_24 = search_links(links_24)
search_link_25 = search_links(links_25)
search_link_26 = search_links(links_26)
search_link_27 = search_links(links_27)
search_link_28 = search_links(links_28)
search_link_29 = search_links(links_29)
search_link_30 = search_links(links_30)
search_link_31 = search_links(links_31)
search_link_32 = search_links(links_32)
search_link_33 = search_links(links_33)
search_link_34 = search_links(links_34)
search_link_35 = search_links(links_35)
search_link_36 = search_links(links_36)
search_link_37 = search_links(links_37)
search_link_38 = search_links(links_38)
search_link_39 = search_links(links_39)
search_link_40 = search_links(links_40)
search_link_41 = search_links(links_41)
search_link_42 = search_links(links_42)
search_link_43 = search_links(links_43)
search_link_44 = search_links(links_44)
search_link_45 = search_links(links_45)
search_link_46 = search_links(links_46)
search_link_47 = search_links(links_47)
search_link_48 = search_links(links_48)
search_link_49 = search_links(links_49)
search_link_50 = search_links(links_50)

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
full_body_33 = uni_parserd_ye102(search_link_33)
full_body_34 = uni_parserd_ye102(search_link_34)
full_body_35 = uni_parserd_ye102(search_link_35)
full_body_36 = uni_parserd_ye102(search_link_36)
full_body_37 = uni_parserd_ye102(search_link_37)
full_body_38 = uni_parserd_ye102(search_link_38)
full_body_39 = uni_parserd_ye102(search_link_39)
full_body_40 = uni_parserd_ye102(search_link_40)
full_body_41 = uni_parserd_ye102(search_link_41)
full_body_42 = uni_parserd_ye102(search_link_42)
full_body_43 = uni_parserd_ye102(search_link_43)
full_body_44 = uni_parserd_ye102(search_link_44)
full_body_45 = uni_parserd_ye102(search_link_45)
full_body_46 = uni_parserd_ye102(search_link_46)
full_body_47 = uni_parserd_ye102(search_link_47)
full_body_48 = uni_parserd_ye102(search_link_48)
full_body_49 = uni_parserd_ye102(search_link_49)
full_body_50 = uni_parserd_ye102(search_link_50)


full_list = full_body_1 + full_body_2 + full_body_3 + full_body_4 + full_body_5 + full_body_6 + full_body_7 + full_body_8 + full_body_9 + full_body_10 + full_body_11 + full_body_12+full_body_13+full_body_14+full_body_15+full_body_16+full_body_17+full_body_18+full_body_19+full_body_20+full_body_21+full_body_22+full_body_23+full_body_24 + full_body_25 +full_body_26 + full_body_27 + full_body_28 + full_body_29 + full_body_30 +full_body_31 + full_body_32 + full_body_33 + full_body_34 + full_body_35 + full_body_36 + full_body_37 + full_body_38 + full_body_39 + full_body_40 + full_body_41 + full_body_42+full_body_43+full_body_44+full_body_45+full_body_46+full_body_47+full_body_48+full_body_49+full_body_50

fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
with open(r'result_kulturarb_4.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list)
