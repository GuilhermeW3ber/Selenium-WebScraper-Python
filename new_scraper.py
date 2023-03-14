from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser = webdriver.Chrome("C:/Users/Guilh/OneDrive/Área de Trabalho/Projetos/Aula Byjus/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    try:
        page=requests.get(hyperlink)
        soap=BeautifulSoup(page.content, "html.parser")
        temp_list=[]
        for tr_tag in soap.find_all("tr", attrs={
            "class":"fact_row"
        }):
            td_tags=tr_tag.find_all("td")
            for td_tag in td_tags:
                try: 
                    temp_list.append(td_tag.find_all("div", attrs={
                        "class":"value"
                    })[0].contents[0])
                except:
                    temp_list.append("")
        new_planets_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

planet_df_1 = pd.read_csv("C:/Users/Guilh/OneDrive/Área de Trabalho/PRO_1-1_C128_AtividadeDoAluno1/updated_scraped_data.csv")

for index, row in planet_df_1.iterrows():
    print(row["hyperlink"])
    scrape_more_data(row["hyperlink"])
    print("Colocando mais dados em Hyperlink", index+1)

print(new_planets_data)

scraped_data = []

for row in new_planets_data:
    replaced = []
    for el in row:
        el=el.replace("\n", "")
        replaced.append(el)

    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scraped_data,columns = headers)

new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
