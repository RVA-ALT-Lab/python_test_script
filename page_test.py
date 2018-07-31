import csv
import requests
import chardet
import time

def check_traffic():
    while True:
        with open('./page_urls.csv', 'rb') as csv_file:
            result = chardet.detect(csv_file.read())
        with open('./page_urls.csv', 'r', encoding=result['encoding']) as encoded_file:
            rows = csv.reader(encoded_file)
            for row in rows:
                url = "http://staging.rampages.us/" + row[0]
                print("getting url: " + url)
                r = requests.get(url)
                res = {"url": url, "status_code": r.status_code, "test": r.text }
                print(res)
                time.sleep(.2)

check_traffic()