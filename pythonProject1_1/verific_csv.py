import fasttext
import csv
model = fasttext.load_model('pyfasttext/models/lid.176.bin')
# classifier = pipeline('text-classification','slone/fastText-LID-323')
clear_row = list()

file_1 = 'result_ataisal.csv'
file_2 = 'result_bash.csv'
file_3 = 'result_bashgazet.csv'
file_4 = 'result_kulturarb.csv'
file_5 = 'result_ye102.csv'
def row_reader(file_f):
    with open(file_f, 'r', encoding='utf-8') as data:
        reader = csv.reader(data)
        for row in reader:
            row_str = row[2].strip().replace('\n',' ')
            lid_result = model.predict(row_str, 3)
            # print(lid_result[0][0], type(lid_result[0][0]))
            if lid_result[0][0] == '__label__ba':
                # print(lid_result[0][0], row)
                dict_content = {
                    'url': row[0],
                    'title': row[1],
                    'content': row[2],
                    'data': row[3],
                    'category': row[4],
                    'tags': row[5]
                }
                clear_row.append(dict_content)
    return clear_row

result_ataisal = row_reader(file_1)
result_bash = row_reader(file_2)
result_bashgazet = row_reader(file_3)
result_kulturarb = row_reader(file_4)
result_ye102 = row_reader(file_5)

full_result = result_ataisal + result_bash + result_bashgazet + result_kulturarb + result_ye102
fieldnames = ['url', 'title', 'content', 'data', 'category', 'tags']
with open(r'clear_result.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(full_result)