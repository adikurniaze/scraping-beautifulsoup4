import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kompas-populer')
def kompas_populer():
    html_kompas_doc = requests.get('https://indeks.kompas.com/terpopuler')
    soup = BeautifulSoup(html_kompas_doc.text, 'html.parser')
    populer_area = soup.find(attrs={'class': 'latest--indeks mt2 clearfix'})
    titles = populer_area.findAll(attrs={'class': 'article__list__title'})
    images = populer_area.findAll(attrs={'class': 'article__asset'})
#    urls = populer_area.find(attrs={'class': 'article__link'})
    urls = populer_area.findAll(attrs={'class': 'article__link'})
    data = populer_area.findAll(attrs={'class': 'article__list'})
    return render_template('index.html', titles=titles, images=images, data=data, urls=urls)

if __name__=='__main__':
    app.run(debug=True)