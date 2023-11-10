import fasttext
import csv
import numpy as np
model = fasttext.load_model('pyfasttext/models/lid.176.bin')
# file = ['result_ataisal.csv', 'result_bash.csv', 'result_bashgazet.csv', 'result_kulturarb.csv', 'result_kulturarb_1.csv', 'result_kulturarb_2.csv', 'result_kulturarb_3.csv', 'result_kulturarb_4.csv', 'result_ye102.csv']

clear_full_url = list()
with open('all_result.csv', 'r', encoding='utf-8') as data:
    reader = csv.reader(data)
    for row in reader:
        dict_content = {
            'url': row[0],
            'title': row[1],
            'lead': row[2],
            'content': row[3],
            'data': row[4],
            'category': row[5],
            'tags': row[6]
        }
        clear_full_url.append(dict_content)

list_item = list()
resultSenceFastext_full = list()
item = {}
hhh =[]
for elem in clear_full_url:
    row_str = elem['content'].strip().replace('\n',' ')
    row_list = row_str.split(".")
    resultSenceFastext = list()
    for sent in row_list:
        if sent == '' or sent == ' ' or sent == '\n' or sent == 'Na':
            row_list.remove(sent)
        else:
            lid_result = model.predict(sent, 3)
            if lid_result[0][0] == '__label__ba':
                resultSenceFastext.append(1)
            else:
                resultSenceFastext.append(-1)
    resultSenceFastext_full.append({
        'rezult' : resultSenceFastext,
        'url' : elem['url'],
        'title' : elem['title'],
        'lead': elem['lead'],
        'content': elem['content'],
        'data': elem['data'],
        'category': elem['category'],
        'tags': elem['tags']
    })
full_list_all = []
full_list_all___2 = []
for i in range(0, len(resultSenceFastext_full)-1):
    if np.sum(resultSenceFastext_full[i]['rezult']) >= 1:
        full_list_all.append(resultSenceFastext_full[i])
for i in range(0, len(full_list_all)-1):
    full_list_all___2.append({
        'rezult' : np.sum(full_list_all[i]['rezult']),
        'url' : full_list_all[i]['url'],
        'title' : full_list_all[i]['title'],
        'lead': full_list_all[i]['lead'],
        'content': full_list_all[i]['content'],
        'data': full_list_all[i]['data'],
        'category': full_list_all[i]['category'],
        'tags': full_list_all[i]['tags']
    })
print(full_list_all___2)

fieldnames = ['rezult','url', 'title', 'lead', 'content', 'data', 'category', 'tags']

with open(r'clear_all_result_111.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_list_all___2)
