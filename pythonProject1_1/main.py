import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# для сайта https://gulshat1.ucoz.net/news/rss/ ВСЕ КАТЕГОРИИ

link = 'https://gulshat1.ucoz.net/news/rss/'

# xml_data  = requests.get(link, headers=headers).content
# def parse_xml(xml_data):
#   # Initializing soup variable
#     soup = BeautifulSoup(xml_data, 'xml')
#
#   # Creating column for table
#     df = pd.DataFrame(columns=['guid', 'title', 'pubDate', 'description'])
#
#   # Iterating through item tag and extracting elements
#     all_items = soup.find_all('item')
#     items_length = len(all_items)
#
#     for index, item in enumerate(all_items):
#         guid = item.find('guid').text
#         title = item.find('title').text
#         pub_date = item.find('pubDate').text
#         description = item.find('description').text
#
#        # Adding extracted elements to rows in table
#         row = {
#             'guid': guid,
#             'title': title,
#             'pubDate': pub_date,
#             'description': description
#         }
#
#         df = df.append(row, ignore_index=True)
#         print(f'Appending row %s of %s' % (index+1, items_length))
#
#     return df
# df = parse_xml(xml_data)
# df.to_csv('news.csv')
def search_links(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    all_links = soup.find_all('item')
    return all_links
list_link = []
# создали список ссылок на статьи
def link_collector(all_links):
    for item in all_links:
        if item not in list_link:
            list_link.append(item.link.text)
    return list_link

def uni_parserd(link):
    title = []
    content = []
    list_dict = []
    for item in link:
        all_url = requests.get(item)
        soup = BeautifulSoup(all_url.content, 'lxml')
        all_content = soup.find_all('html')
        for elem in all_content:
            if elem not in list_dict:
                title.append(elem.find('div', class_='eTitle').text)
                content.append(elem.find('td',class_='eMessage').text)
    return title, content

def search_cat(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    all_category = soup.find_all('item')
    cat_list = []
    for g in all_category:
        cat_list.append(g.find('dc:creator').text)
    return cat_list

search_links_1 = search_links(link)
link_collector_1 = link_collector(search_links_1)
uni_parserd_full = uni_parserd(list_link)
list_category_1 = search_cat(link)

full_title_1 = uni_parserd_full[0]
full_content_1 = uni_parserd_full[1]
# для сайта https://kulturarb.ru/ba/news


link_2 = 'https://kulturarb.ru/ba/news'

# создали список ссылок на статьи
def search_links_2(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//h4[@class="item-title"]/a/@href')

    return all_links
full_link_list = []
def uni_parserd_2(link):
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
full_content = uni_parserd_2(search_link)

full_title = full_content[0]
full_content = full_content[1]
list_cat_2 =search_cat_2(full_title)

# для сайта https://www.ye02.ru/rss.xml ВСЕ КАТЕГОРИИ
link_3 = 'https://www.ye02.ru/rss.xml'

def uni_parserd_3(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    all_item = soup.find_all('item')
    title = []
    content = []
    for k in all_item:
        title.append(k.find('title').text)
        content.append(k.find('turbo:content').text)
    return title, content

def search_cat_3(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    all_category = soup.find_all('item')
    cat_list = []
    for g in all_category:
        cat_list.append(g.find('category').text)
    return cat_list

content_3 = uni_parserd_3(link_3)
full_title_3 = content_3[0]
full_content_3 = content_3[1]
list_category_3 = search_cat_3(link_3)

# для сайта https://misrbash.moy.su/news/rss/ ВСЕ КАТЕГОРИИ
link_4 = 'https://misrbash.moy.su/news/rss/'

def uni_parserd_4(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    all_item = soup.find_all('item')
    title = []
    content = []
    for k in all_item:
        title.append(k.find('title').text)
        content.append(k.find('content:encoded').text)
    return title, content

def search_cat_4(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    all_category = soup.find_all('item')
    cat_list = []
    for g in all_category:
        cat_list.append(g.find('creator').text)
    return cat_list

content_4 = uni_parserd_4(link_4)
full_title_4 = content_4[0]
full_content_4 = content_4[1]
list_category_4 = search_cat_4(link_4)
# для сайта https://bashgazet.ru/articles/-bi-t-m-m-ni-t КУЛЬТУРА

link_5 = 'https://bashgazet.ru/articles/-bi-t-m-m-ni-t'

# создали список ссылок на статьи
def search_links_5(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

full_link_list_5 = []
def uni_parserd_5(link):
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
full_content_5 = uni_parserd_5(search_link_5)

full_title_5 = full_content_5[0]
full_content_5 = full_content_5[1]
list_cat_5 =search_cat_5(full_title_5)


# для сайта https://ataisal.com/articles/m-ni-t КУЛЬТУРА

link_6 = 'https://ataisal.com/articles/m-ni-t'

# создали список ссылок на статьи
def search_links_6(link):
    url = requests.get(link)

    soup = BeautifulSoup(url.content, 'html.parser')
    dom = etree.HTML(str(soup))
    all_links = dom.xpath('//a[@class="item item"]/@href')
    return all_links

full_link_list_6 = []
def uni_parserd_6(link):
    for item in link:
        if item not in full_link_list_6:
            full_link = 'https://bashgazet.ru'+item
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
        catgory_2.append('мәҙәниәт')
    return catgory_2

search_link_6 = search_links_6(link_6)
full_content_6 = uni_parserd_6(search_link_6)

full_title_6 = full_content_6[0]
full_content_6 = full_content_6[1]
list_cat_6 = search_cat_6(full_title_6)

# сбор всех заголовков и текстов в один список, для премещения в словарь
title_list = full_title_1 + full_title + full_title_3 + full_title_4 + full_title_5 + full_title_6
content_list = full_content_1 + full_content + full_content_3 + full_content_4 + full_content_5 + full_content_6
category_list = list_category_1 + list_cat_2 + list_category_3 + list_category_4 + list_cat_5 + list_cat_6
print(len(title_list))
print(len(content_list))
print(len(category_list))
all_dict = {'Title': title_list, 'Content': content_list, 'Category': category_list}

content_frame = pd.DataFrame(all_dict)

content_frame.to_csv (r'result.csv', index= False )
