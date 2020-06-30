import requests
from bs4 import BeautifulSoup

#Cari berita kompas populer
html_kompas_doc = requests.get('https://indeks.kompas.com/terpopuler')
soup = BeautifulSoup(html_kompas_doc.text, 'html.parser')
populer_area = soup.find(attrs={'class': 'latest--indeks mt2 clearfix'})
titles = populer_area.findAll(attrs={'class': 'article__list__title'})
images = populer_area.findAll(attrs={'class': 'article__list'})
urls = populer_area.findAll(attrs={'class': 'article__link'})

print(images)

