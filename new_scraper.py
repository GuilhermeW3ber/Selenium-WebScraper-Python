from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# URL dos Exoplanetas da NASA
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    
    ## ADICIONE O CÓDIGO AQUI ##







planet_df_1 = pd.read_csv("updated_scraped_data.csv")

# Chame o método
for index, row in planet_df_1.iterrows():

    ## ADICIONE O CÓDIGO AQUI ##

     # Call scrape_more_data(<hyperlink>)

    print(f"Coleta de dados do hyperlink {index+1} concluída")

print(new_planets_data)

# Remova o caractere '\n' dos dados coletados
scraped_data = []

for row in new_planets_data:
    replaced = []
    ## ADICIONE O CÓDIGO AQUI ##


    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)

# Converta para CSV
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
