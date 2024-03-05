from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    start_date = str(request.form['start_date'])
    end_date = str(request.form['end_date'])
    print(start_date, end_date)
    dictionary = []
    res = requests.get('https://data.calgary.ca/resource/c2es-76ed.geojson?', params = {"$where": 'issueddate' > start_date and 'issueddate' < end_date})
    info = res.json()
    if 'features' in info and info['features']:
        for item in info['features']:
            print(item)
            data = item['geometry']
            print(data)
            latitude = data.get('coordinates')[0]
            longitude = data.get('coordinates')[1]  
            data1 = item['properties']
            permit = data1.get('permitnum')
            date = data1.get('issueddate')
            name = data1.get('contractorname')
            type = data1.get('permittype')
            if latitude and longitude:
                dictionary.append({'latitude': latitude, 'longitude': longitude, 'permit':permit, 'date':date, 'name': name, 'type':type})
                print(dictionary)
    
    # Process the start_date and end_date as needed for your API request
    # You can use the values in your API request to https://data.calgary.ca/resource/c2es-76ed.geojson

    # For demonstration, let's just return the selected date range
    print(dictionary)
    return jsonify({'start_date': start_date, 'end_date': end_date})

if __name__ == '__main__':
    app.run(debug=True)


    #In order to run the code type python -m flask run in the command line
    # run this first at the beginning of the session  $env:FLASK_APP = "application.py"


