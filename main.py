import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

reponse = requests.get(url)

if reponse.ok:
    print(reponse.content)
    page = reponse.content

    soup = BeautifulSoup(page, 'html.parser')

    product_page_url = url
    print(url)

    titre_bs = soup.find("h1")
    print(titre_bs.text)

    #table
    data = []
    table = soup.find('table', {"class": "table table-striped"})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')















