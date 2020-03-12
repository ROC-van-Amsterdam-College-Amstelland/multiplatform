# importeer libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Geef de url in een variabele
url = ''

# query de website en sla deze op in de variabele `pagina`
pagina = 

# parse de html door gebruik te maken van BeautifulSoupo en sla deze op in `soep`
soep = 


title = soep.find()
print (title.string)

table = soep.find()
# print (table)

all_movies = table.find_all()
# print (second.a.contents[0])

print (all_movies)

movie_nmbr_1 = table.find()
print (movie_nmbr_1)