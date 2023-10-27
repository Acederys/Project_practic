from langdetect import detect
from langdetect import detect_langs
import cld2
import csv
# classifier = pipeline('text-classification','slone/fastText-LID-323')
with open('result_ataisal.csv', 'r', encoding='utf-8') as data:
    reader = csv.reader(data)
    for row in reader:
        print(row[2])
        print(cld2.detect(row[2]))
