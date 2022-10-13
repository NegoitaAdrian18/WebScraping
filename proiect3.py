"""
beoxl.nl      ==>> Vezi "Proiect3.csv.csv"
"""

from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

Nume = []
Pret = []
Raiting = []


with open('Proiect3.csv', 'w', encoding='utf8', newline='') as p:
    scrie = writer(p)

    pag_nr = 147
    for i in range(1, int(pag_nr) +1):
        url = "https://beoxl.nl/collections/hond?page="+str(i)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        lista = soup.find_all('a', class_='prod-th')

        for info in lista:
            titlu = info.find('span', class_='title').text.replace('\n', '')
            Nume.append(titlu)

            pret = info.find('span', class_='price').text.replace('\n', '')
            Pret.append(pret)

            # raiting = info.find('div', class_='wwk-widget__reviews_count').text.replace('\n', '')
            # Raiting.append(raiting)

date = pd.DataFrame({'Nume': Nume, 'Pret': Pret})
date.to_csv('Proiect3.csv')