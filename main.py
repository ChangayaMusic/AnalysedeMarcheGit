import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, 'html.parser')

titre = soup.find("h1")

cat = soup.find_all("th")
categories = []
categories.append(cat)

info = soup.find_all("td")
informations = []
informations.append(info)

print(categories)
print(informations)

en_tete = [titre, url]


with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    for cat, info in zip(informations, categories):
        writer.writerow([categories, informations])







































