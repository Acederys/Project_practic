import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

# все ссылки
# общество
link_1 = 'https://ye102.ru/articles/obschestvo'
# культура
link_2 = 'https://kulturarb.ru/ba/news'
# экономика
link_3 = 'https://ye102.ru/articles/ek'
# культура
link_5 = 'https://bashgazet.ru/articles/-bi-t-m-m-ni-t'
# экология
link_6 = 'https://ataisal.com/articles/ekologiya'
# экономика
link_7 = 'https://bash.bashinform.ru/news/economy'
# политика
link_8 = 'https://bashgazet.ru/articles/s-y-s-t-m-kho-u'
# спорт
link_9 = 'https://bashgazet.ru/articles/sport-m-turizm'
# экология
link_10 = 'https://bashgazet.ru/articles/ekologiya '
# культура
link_11 = 'https://ataisal.com/articles/m-ni-t '
# спорт
link_12 = 'https://ye102.ru/articles/sport'

def search_links(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

def uni_parserd_kulturarb(link):
    full_link_list = []
    for item in link:
        if item not in full_link_list:
            full_link = 'https://kulturarb.ru/'+item
            full_link_list.append(full_link)
    title = []
    content = []
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='item-title').text)
            content.append(j.find('div', class_='item-text').text)
    return title, content

def uni_parserd_ye102(link):
    full_link_list = []
    for item in link:
        if item not in full_link_list:
            full_link = 'https://ye102.ru'+item
            full_link_list.append(full_link)
    title = []
    content = []
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def uni_parserd_bashgazet(link):
    full_link_list = []
    for item in link:
        if item not in full_link_list:
            full_link = 'https://bashgazet.ru'+item
            full_link_list.append(full_link)
    title = []
    content = []
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def uni_parserd_ataisal(link):
    full_link_list = []
    for item in link:
        if item not in full_link_list:
            full_link = 'https://ataisal.com'+item
            full_link_list.append(full_link)
    title = []
    content = []
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def uni_parserd_bash_bashinform(link):
    full_link_list = []
    for item in link:
        if item not in full_link_list:
            full_link = 'https://bash.bashinform.ru'+item
            full_link_list.append(full_link)
    title = []
    content = []
    for elem in full_link_list:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def add_cat_Kultura(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('мәҙәниәт')
    return catgory_2

def add_cat_sport(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Спорт')
    return catgory_2

def add_cat_society(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Йәмғиәт')
    return catgory_2

def add_cat_politic(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Сәйәсәт һәм хоҡуҡ')
    return catgory_2

def add_cat_economy(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Иҡтисад')
    return catgory_2

def add_cat_ecology(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Экологияһ')
    return catgory_2

search_link_1 = search_links(link_1)
search_link_2 = search_links(link_2)
search_link_3 = search_links(link_3)
search_link_5 = search_links(link_5)
search_link_6 = search_links(link_6)
search_link_7 = search_links(link_7)
search_link_8 = search_links(link_8)
search_link_9 = search_links(link_9)
search_link_10 = search_links(link_10)
search_link_11 = search_links(link_11)
search_link_12 = search_links(link_12)

full_body_1 = uni_parserd_ye102(search_link_1)
full_body_2 = uni_parserd_kulturarb(search_link_2)
full_body_3 = uni_parserd_ye102(search_link_3)
full_body_5 = uni_parserd_bashgazet(search_link_5)
full_body_6 = uni_parserd_ataisal(search_link_6)
full_body_7 = uni_parserd_bash_bashinform(search_link_7)
full_body_8 = uni_parserd_bashgazet(search_link_8)
full_body_9 = uni_parserd_bashgazet(search_link_9)
full_body_10 = uni_parserd_bashgazet(search_link_10)
full_body_11 = uni_parserd_ataisal(search_link_11)
full_body_12 = uni_parserd_ye102(search_link_12)

full_title_1 = full_body_1[0]
full_title_2 = full_body_2[0]
full_title_3 = full_body_3[0]
full_title_5 = full_body_5[0]
full_title_6 = full_body_6[0]
full_title_7 = full_body_7[0]
full_title_8 = full_body_8[0]
full_title_9 = full_body_9[0]
full_title_10 = full_body_10[0]
full_title_11 = full_body_11[0]
full_title_12 = full_body_12[0]

full_content_1 = full_body_1[1]
full_content_2 = full_body_2[1]
full_content_3 = full_body_3[1]
full_content_5 = full_body_5[1]
full_content_6 = full_body_6[1]
full_content_7 = full_body_7[1]
full_content_8 = full_body_8[1]
full_content_9 = full_body_9[1]
full_content_10 = full_body_10[1]
full_content_11 = full_body_11[1]
full_content_12 = full_body_12[1]

list_cat_1 = add_cat_society(full_title_1)
list_cat_2 = add_cat_Kultura(full_title_2)
list_cat_3 = add_cat_economy(full_title_3)
list_cat_5 = add_cat_Kultura(full_title_5)
list_cat_6 = add_cat_ecology(full_title_6)
list_cat_7 = add_cat_economy(full_title_7)
list_cat_8 = add_cat_politic(full_title_8)
list_cat_9 = add_cat_sport(full_title_9)
list_cat_10 = add_cat_ecology(full_title_10)
list_cat_11 = add_cat_Kultura(full_title_11)
list_cat_12 = add_cat_sport(full_title_12)

title_list = full_title_1 + full_title_2 + full_title_3 + full_title_5 + full_title_6 + full_title_7 + full_title_8 + full_title_9 + full_title_10 + full_title_11 + full_title_12
content_list = full_title_1 + full_content_2 + full_content_3 + full_content_5 + full_content_6 + full_content_7 + full_content_8 + full_content_9 + full_content_10 + full_content_11 + full_content_12
category_list = list_cat_2 + list_cat_1 + list_cat_3 + list_cat_5 + list_cat_6 + list_cat_7 + list_cat_8 + list_cat_9 + list_cat_10 + list_cat_11 + list_cat_12
all_dict = {'Title': title_list, 'Content': content_list, 'Category': category_list}
# собираем все в файл
content_frame = pd.DataFrame(all_dict)

content_frame.to_csv (r'result.csv', index= False )
