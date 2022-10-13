"""
https://petcart.nl/product-category/hond/?product-page=2     ==>> Vezi "Proiect4.csv.csv"
"""

from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

Nume = []
Pret = []
Raiting = []


with open('Proiect5.csv', 'w', encoding='utf8', newline='') as p:
    scrie = writer(p)

    pag_nr = 306
    for i in range(1, int(pag_nr) +1):
        url = "https://petcart.nl/product-category/hond/?product-page="+str(i)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        lista = soup.find_all('div', class_='ht-product')

        for info in lista:
            titlu = info.find('h3', class_='ht-product-title')
            Nume.append(titlu)
            print(titlu)

            pret = info.find('span', class_='price').text
            Pret.append(pret)

            #raiting = info.find('div', class_='ht-product-ratting-wrap').text

date = pd.DataFrame({'Nume': Nume, 'Pret': Pret})
date.to_csv('Proiect5.csv')