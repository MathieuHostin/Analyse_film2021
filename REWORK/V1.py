## Library
# pip install webdriver-manager
# pip install selenium

## Library
import csv
import time
import random
import codecs
import sys

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


## Options en tout genre
# fonction pause
def pause():
    time_break = random.randint(1,2)
    return time.sleep(time_break)


# options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
pause()


## On allume le driver
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=options)
driver.maximize_window()
driver.get('https://www.google.com')
wait = WebDriverWait(driver, 30)


début = "https://www.senscritique.com/liste/Recapitulatif_des_films_vus_en_2021/2914300"

driver.get(début) # On va sur la page

pause()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='fc-button fc-cta-consent fc-primary-button']"))).click() #Pour cliquer sur le bouton des cookies lors de la première page d'ouverture
pause()

html = driver.find_element_by_xpath("//body").get_attribute('outerHTML')
print(html)

soup = bs(html, "lxml")
print(soup)

def SCRAPT():
    titre_films = soup.find_all("a", class_="Text__SCText-sc-14ie3lm-0 Link__SecondaryLink-sc-1vfcbn2-1 dGWsbQ jLGgsY ProductListItem__StyledProductTitle-sc-ico7lo-3 ivaIVy")
    d_film = [titre.get_text() for titre in titre_films]
    print(d_film)

    realisateurs = soup.find_all("p", class_="Text__SCText-sc-14ie3lm-0 Creators__Text-sc-1t34n5u-0 dsSNGq hqDnDC ProductListItem__StyledCreators-sc-ico7lo-6 cMTDEQ")
    d_real = [real.get_text() for real in realisateurs]
    print(d_real)

    infos = soup.find_all("p", class_="Text__SCText-sc-14ie3lm-0 ProductListItem__WrapperInfos-sc-ico7lo-10 dsSNGq jCkbVW")
    d_infos = [info.get_text() for info in infos]
    print(d_infos)

    ma_notes = soup.find_all("p", class_="Text__SCText-sc-14ie3lm-0 ProductListItem__AuthorInfo-sc-ico7lo-7 dsSNGq imHvnG")
    d_manote = [ma_note.get_text() for ma_note in ma_notes]
    print(d_manote)

    moyennes = soup.find_all("div", class_="Rating__GlobalRating-sc-1rkvzid-4 lhCdNc Poster__GlobalRating-sc-1jujjag-6 dDuFLw globalRating")
    d_moyenne = [moyenne.get_text() for moyenne in moyennes]
    print(d_moyenne)

SCRAPT()

driver.find_element_by_xpath("//span[. = '2']").click()
pause()
html = driver.find_element_by_xpath("//body").get_attribute('outerHTML')
soup = bs(html, "lxml")

SCRAPT()

# end
print("Bravo !")

driver.close()
