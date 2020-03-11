# importeer libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Geef de url in een variabele
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# query de website en sla deze op in de variabele `pagina`
pagina = urlopen(url)

# parse de html door gebruik te maken van BeautifulSoupo en sla deze op in `soep`
soep = BeautifulSoup(pagina, 'html.parser')


title = soep.find('h1', attrs={'class': 'header'})
print (title.string)

table = soep.find('table', attrs={'class': 'chart full-width'})
# print (table)

all_movies = table.find_all('td', attrs={'class': 'titleColumn'})
# print (second.a.contents[0])

print (all_movies)

movie_nmbr_1 = table.find('td', attrs={'class': 'titleColumn'})
print (movie_nmbr_1.a.contents[0])