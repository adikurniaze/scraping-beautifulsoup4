import requests
from bs4 import BeautifulSoup

#Cari berita kompas populer
html_kompas_doc = requests.get('https://indeks.kompas.com/terpopuler')
soup = BeautifulSoup(html_kompas_doc.text, 'html.parser')
populer_area = soup.find(attrs={'class': 'latest--indeks'})
#populer_area = soup.find(attrs={'class': 'article__list'})
titles = populer_area.findAll(attrs={'class': 'article__list__title'})
images = populer_area.findAll(attrs={'class': 'article__asset'})
urls = populer_area.findAll(attrs={'class': 'article__link'})
data = populer_area.find(attrs={'class': 'article__list'})
print(data.find('img'), data.find('a')['href'] )

#print(data)