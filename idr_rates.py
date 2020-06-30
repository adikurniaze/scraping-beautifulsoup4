import requests

#json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":7.0082139790975e-5,"date":"Tue, 30 Jun 2020 00:00:02 GMT","inverseRate":14268.970710406},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.2196522461336e-5,"date":"Tue, 30 Jun 2020 00:00:02 GMT","inverseRate":16078.069326491}}
#print(json_data)
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])