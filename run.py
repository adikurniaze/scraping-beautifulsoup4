import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

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
    return render_template('kompas-scraper.html', titles=titles, images=images, data=data, urls=urls)

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas=json_data.values())


if __name__=='__main__':
    app.run(debug=True)