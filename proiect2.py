"""
https://www.petshop24.nl/     ==>> Vezi "Proiect2.csv.csv"
"""

from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

Nume = []
Pret = []
Raiting = []


with open('Proiect2.csv', 'w', encoding='utf8', newline='') as p:
    scrie = writer(p)

    pag_nr = 711
    for i in range(1, int(pag_nr) +1):
        url = "https://www.petshop24.nl/product-category/hond/page/"+str(i)+"/"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        lista = soup.find_all('div', class_='product-small')

        for info in lista:
            titlu = info.find('div', class_='title-wrapper').text.replace('\n', '')
            Nume.append(titlu)

            pret = info.find('span', class_='woocommerce-Price-amount amount').text.replace('\n', '')
            Pret.append(pret)

            # raiting = info.find('div', class_='wwk-widget__reviews_count').text.replace('\n', '')
            # Raiting.append(raiting)

date = pd.DataFrame({'Nume': Nume, 'Pret': Pret})
date.to_csv('Proiect2.csv')