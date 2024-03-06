from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import requests


start_date = "'2020-01-21'"
end_date = "'2020-01-23'"
print(start_date, end_date)
res = requests.get('https://data.calgary.ca/resource/c2es-76ed.geojson?', params = {"$where": 'issueddate' > start_date and 'issueddate' < end_date })
info = res.json()
print(info)
if 'features' in info:
        print('key is present')
        x = info['features']
        print(x)
        for item in info['features']:
            print('looping')
            print(item)
        print('for loop does not work')
            
            