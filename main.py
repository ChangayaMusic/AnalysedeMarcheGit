import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

reponse = requests.get(url)

if reponse.ok:
    print(reponse.content)
    page = reponse.text

    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)
    product_page_url = url
    #print(url)

    titre_bs = soup.find("h1")
    print(titre_bs.text)

    book_table = soup.find('table', class_ = 'table table-striped').text
    #print(book_table)

    rows = soup.find_all('tr')

    for row in rows:
        categorie = row.find('th').text
        #print(categorie)
        inforations = row.find('td').text
        #print(inforations)

    catinfo = categorie + inforations

























