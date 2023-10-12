import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
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
# для сайта gulshat1.ucoz.net
search_links(link)
link_collector(search_links(link))
uni_parserd(list_link)


title_dict = uni_parserd(list_link)[0]
content_dict = uni_parserd(list_link)[1]
all_dict = {'Title': title_dict, 'Content': content_dict}

content_frame = pd.DataFrame(all_dict)

content_frame.to_csv (r' result.csv', index= False )
