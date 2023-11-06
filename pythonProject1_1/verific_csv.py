import fasttext
import csv
model = fasttext.load_model('pyfasttext/models/lid.176.bin')
file = ['result_ataisal.csv', 'result_bash.csv', 'result_bashgazet.csv','result_kulturarb.csv', 'result_ye102.csv']

clear_full_url = list()
for url in file:
    with open(url, 'r', encoding='utf-8') as data:
        reader = csv.reader(data)
        for row in reader:
            dict_content = {
                'url': row[0],
                'title': row[1],
                'lead': row[2],
                'contgient': row[3],
                'data': row[4],
                'category': row[5],
                'tags': row[6]
            }
            clear_full_url.append(dict_content)

list_item = list()
for elem in clear_full_url:
    row_str = elem['content'].strip().replace('\n',' ')
    lid_result = model.predict(row_str, 3)
    if lid_result[0][0] == '__label__ba':
        list_item.append(elem)

fieldnames = ['url', 'title', 'lead', 'content', 'data', 'category', 'tags']
with open(r'clear_result_test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_item)