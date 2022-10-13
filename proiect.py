
"""
https://www.petinboots.com/     ==>> Vezi "primul_site.csv"
"""
from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

Nume = []
Pret = []
Rating = []


with open('primul_site.csv', 'w', encoding='utf8', newline='') as fff:
    thewriter = writer(fff)
    #header = ['Titlu', 'Pret', 'Rating']
    #thewriter.writerow(header)


    page_nr = 143
    for i in range(1, int(page_nr)+1):
        url = "https://huisdiershopper.nl/collections/hond?page=" + str(i) + "&grid_list=grid-view"
        req = requests.get(url)

        soup = BeautifulSoup(req.content, "html.parser") # am realizat un obiect ce contine continutul paginii
        lista = soup.find_all('div', class_="productitem")




        # for item in lista:
        #     item_info = soup.find_all('div', class_="productitem--info")

        for info in lista:
            titlu = info.find("h2", class_="productitem--title").text.replace('\n', '')
            Nume.append(titlu)

            pret = info.find("span", class_="money").text.replace('\n', '')
            Pret.append(pret)

            raiting = info.find("span", class_="spr-starrating spr-badge-starrating").text.replace('\n', '')
            Rating.append(raiting)

date = pd.DataFrame({'Nume': Nume, 'Pret': Pret, 'Rating': Rating})
date.to_csv('primul_site.csv')
