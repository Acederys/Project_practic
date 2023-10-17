# ТЕСТОВЫЙ ЧЕРНОВОЙ ВАРИАНТ

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

# для сайта https://kulturarb.ru/ba/news КУЛЬТУРА
link_2 = 'https://kulturarb.ru/ba/news'

# создали список ссылок на статьи
def search_links_2(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//h4[@class="item-title"]/a/@href')

    return all_links

def uni_parserd_2(link):
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

def search_cat_2(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('мәҙәниәт')
    return catgory_2

search_link = search_links_2(link_2)
full_body = uni_parserd_2(search_link)

full_title = full_body[0]
full_content = full_body[1]
list_cat_2 =search_cat_2(full_title)

# для сайта https://www.ye02.ru/rss.xml ВСЕ КАТЕГОРИИ
# link_3 = 'https://www.ye02.ru/rss.xml'
#
# def uni_parserd_3(link):
#     url = requests.get(link)
#     soup = BeautifulSoup(url.content, 'xml')
#     all_item = soup.find_all('item')
#     title = []
#     content = []
#     for k in all_item:
#         title.append(k.find('title').text)
#         content.append(k.find('turbo:content').text)
#     return title, content
#
# def search_cat_3(link):
#     url = requests.get(link)
#     soup = BeautifulSoup(url.content, 'xml')
#     all_category = soup.find_all('item')
#     cat_list = []
#     for g in all_category:
#         cat_list.append(g.find('category').text)
#     return cat_list
#
# content_3 = uni_parserd_3(link_3)
# full_title_3 = content_3[0]
# full_content_3 = content_3[1]
# list_category_3 = search_cat_3(link_3)

# для сайта https://misrbash.moy.su/news/rss/ ВСЕ КАТЕГОРИИ
# link_4 = 'https://misrbash.moy.su/news/rss/'
#
# def uni_parserd_4(link):
#     url = requests.get(link)
#     soup = BeautifulSoup(url.content, 'xml')
#     all_item = soup.find_all('item')
#     title = []
#     content = []
#     for k in all_item:
#         title.append(k.find('title').text)
#         content.append(k.find('content:encoded').text)
#     return title, content
#
# def search_cat_4(link):
#     url = requests.get(link)
#     soup = BeautifulSoup(url.content, 'xml')
#     all_category = soup.find_all('item')
#     cat_list = []
#     for g in all_category:
#         if g.find('category').text  == True:
#             cat_list.append(g.find('category').text)
#         else:
#             cat_list.append('')
#     return cat_list
# content_4 = uni_parserd_4(link_4)
# full_title_4 = content_4[0]
# full_content_4 = content_4[1]
# list_category_4 = search_cat_4(link_4)

# для сайта https://bashgazet.ru/articles/-bi-t-m-m-ni-t КУЛЬТУРА

link_5 = 'https://bashgazet.ru/articles/-bi-t-m-m-ni-t'

# создали список ссылок на статьи
def search_links_5(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links


def uni_parserd_5(link):
    full_link_list_5 = []
    for item in link:
        if item not in full_link_list_5:
            full_link = 'https://bashgazet.ru'+item
            full_link_list_5.append(full_link)
    # print(full_link_list_5)
    title = []
    content = []
    for elem in full_link_list_5:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def search_cat_5(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('мәҙәниәт')
    return catgory_2

search_link_5 = search_links_5(link_5)
full_body_5 = uni_parserd_5(search_link_5)

full_title_5 = full_body_5[0]
full_content_5 = full_body_5[1]
list_cat_5 =search_cat_5(full_title_5)


# для сайта https://ataisal.com/articles/ekologiya ЭКОЛОГИЯ

link_6 = 'https://ataisal.com/articles/ekologiya'

# создали список ссылок на статьи
def search_links_6(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links


def uni_parserd_6(link):
    full_link_list_6 = []
    for item in link:
        if item not in full_link_list_6:
            full_link = 'https://ataisal.com'+item
            full_link_list_6.append(full_link)
    title = []
    content = []
    for elem in full_link_list_6:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def search_cat_6(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Экологияһ')
    return catgory_2

search_link_6 = search_links_6(link_6)
full_body_6 = uni_parserd_6(search_link_6)

full_title_6 = full_body_6[0]
full_content_6 = full_body_6[1]
list_cat_6 = search_cat_6(full_title_6)

# для сайта https://bash.bashinform.ru/news/economy ЭКОНОМИКА
link_7 = 'https://bash.bashinform.ru/news/economy'

# создали список ссылок на статьи
def search_links_7(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

def uni_parserd_7(link):
    full_link_list_7 = []
    for item in link:
        if item not in full_link_list_7:
            full_link = 'https://bash.bashinform.ru'+item
            full_link_list_7.append(full_link)
    title = []
    content = []
    for elem in full_link_list_7:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def search_cat_7(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Иҡтисад')
    return catgory_2

search_link_7 = search_links_7(link_7)
full_body_7 = uni_parserd_7(search_link_7)

full_title_7 = full_body_7[0]
full_content_7 = full_body_7[1]
list_cat_7 = search_cat_7(full_title_7)

# для сайта https://bashgazet.ru/articles/s-y-s-t-m-kho-u Политика
link_8 = 'https://bashgazet.ru/articles/s-y-s-t-m-kho-u'
# создали список ссылок на статьи
def search_links_8(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

def uni_parserd_8(link):
    full_link_list_8 = []
    for item in link:
        if item not in full_link_list_8:
            full_link = 'https://bashgazet.ru'+item
            full_link_list_8.append(full_link)
    title = []
    content = []
    for elem in full_link_list_8:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def search_cat_8(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Сәйәсәт һәм хоҡуҡ')
    return catgory_2

search_link_8 = search_links_8(link_8)
full_body_8 = uni_parserd_8(search_link_8)

full_title_8 = full_body_8[0]
full_content_8 = full_body_8[1]
list_cat_8 = search_cat_8(full_title_8)

# для рубрики https://bashgazet.ru/articles/sport-m-turizm СПОРТ + ТУРИЗМ
link_9 = 'https://bashgazet.ru/articles/sport-m-turizm'
def search_cat_9(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Спорт')
    return catgory_2

search_link_9 = search_links_8(link_9)
full_content_9 = uni_parserd_8(search_link_9)

full_title_9 = full_content_9[0]
full_content_9 = full_content_9[1]
list_cat_9 = search_cat_9(full_title_9)

# для рубрики https://bashgazet.ru/articles/ekologiya ЭКОЛОГИЯ
link_10 = 'https://bashgazet.ru/articles/ekologiya '
def search_cat_10(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Экологияһы')
    return catgory_2

search_link_10 = search_links_8(link_10)
full_body_10 = uni_parserd_8(search_link_10)

full_title_10 = full_body_10[0]
full_content_10 = full_body_10[1]
list_cat_10 = search_cat_10(full_title_10)

# для https://ye102.ru/articles/obschestvo ОБЩЕСТВО

link_1 = 'https://ye102.ru/articles/obschestvo'

# создали список ссылок на статьи
def search_links_1(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

def uni_parserd_1(link):
    full_link_list_1 = []
    for item in link:
        if item not in full_link_list_1:
            full_link = 'https://ye102.ru'+item
            full_link_list_1.append(full_link)
    title = []
    content = []
    for elem in full_link_list_1:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

def search_cat_1(full_title):
    catgory_2 =[]
    i=0
    for i in range(len(full_title)):
        i+=1
        catgory_2.append('Йәмғиәт')
    return catgory_2

search_link_1 = search_links_1(link_1)
full_body_1 = uni_parserd_1(search_link_1)

full_title_1 = full_body_1[0]
full_content_1 = full_body_1[1]
list_cat_1 = search_cat_1(full_title_1)

# Для рубрики https://ye102.ru/articles/ek
link_3 = 'https://ye102.ru/articles/ek'

search_link_3 = search_links_1(link_3)
full_body_3 = uni_parserd_1(search_link_3)

full_title_3 = full_body_3[0]
full_content_3 = full_body_3[1]
list_cat_3 = search_cat_7(full_title_3)

# # для рубрики https://ye102.ru/articles/pl Политика
# link_4 = 'https://ye102.ru/articles/pl'
#
# search_link_4 = search_links_1(link_4)
# full_body_4 = uni_parserd_1(search_link_4)
#
# full_title_4 = full_body_4[0]
# full_content_4 = full_body_4[1]
# list_cat_4 = search_cat_8(full_title_4)

# для рубрики https://ye102.ru/articles/sport СПОРТ

link_12 = 'https://ye102.ru/articles/sport'

search_link_12 = search_links_1(link_12)
full_body_12 = uni_parserd_1(search_link_12)

full_title_12 = full_body_12[0]
full_content_12 = full_body_12[1]
list_cat_12 = search_cat_9(full_title_12)

# https://ataisal.com/articles/m-ni-t КУЛЬТУРА

link_11 = 'https://ataisal.com/articles/m-ni-t '

def uni_parserd_11(link):
    full_link_list_11 = []
    for item in link:
        if item not in full_link_list_11:
            full_link = 'https://ataisal.com'+item
            full_link_list_11.append(full_link)
    title = []
    content = []
    for elem in full_link_list_11:
        url = requests.get(elem)
        soup = BeautifulSoup(url.content, 'html.parser')
        all_content = soup.find_all('body')
        for j in all_content:
            title.append(j.find('h1', class_='h1').text)
            content.append(j.find('div', class_='paragraph serif-text').text)
    return title, content

search_link_11 = search_links_1(link_11)
full_body_11 = uni_parserd_1(search_link_11)

full_title_11 = full_body_11[0]
full_content_11 = full_body_11[1]
list_cat_11 = search_cat_2(full_title_11)

# сбор всех заголовков и текстов в один список, для премещения в словарь
title_list = full_title + full_title_1 + full_title_3 + full_title_5 + full_title_6 + full_title_7 + full_title_8 + full_title_9 + full_title_10 + full_title_11 + full_title_12
content_list = full_content + full_content_1 + full_content_3 + full_content_5 + full_content_6 + full_content_7 + full_content_8 + full_content_9 + full_content_10 + full_content_11 + full_content_12
category_list = list_cat_2 + list_cat_1 + list_cat_3 + list_cat_5 + list_cat_6 + list_cat_7 + list_cat_8 + list_cat_9 + list_cat_10 + list_cat_11 + list_cat_12
print(len(title_list))
print(len(content_list))
print(len(category_list))
all_dict = {'Title': title_list, 'Content': content_list, 'Category': category_list}

content_frame = pd.DataFrame(all_dict)

content_frame.to_csv (r'result.csv', index= False )
