from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

permit_data = [
    {"latitude": 51.0527, "longitude": -114.0719, "permit_number": "PERMIT001", "date": "2022-03-01"},
    {"latitude": 51.0447, "longitude": -114.0710, "permit_number": "PERMIT002", "date": "2022-03-05"},
    {"latitude": 51.0560, "longitude": -114.0715, "permit_number": "PERMIT003", "date": "2022-03-10"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    dictionary = []
    start_date = str(request.form['start_date'])
    end_date = str(request.form['end_date'])
    #print(start_date, end_date)
    api_url = "https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate>'%s'and issueddate<'%s'" %(start_date, end_date)
    res = requests.get(api_url)
    #res = requests.get('https://data.calgary.ca/resource/c2es-76ed.geojson?', params = {"$where": 'issueddate' > start_date and 'issueddate' < end_date })
    info = res.json()
    if 'features' in info and info['features']:
        for item in info['features']:
            #print(item)
            data = item['geometry']
            #print(data)
            latitude = data.get('coordinates')[0]
            longitude = data.get('coordinates')[1]  
            data1 = item['properties']
            permit = str(data1.get('permitnum'))
            date = str(data1.get('issueddate'))
            name = data1.get('contractorname')
            type = data1.get('permittype')
            if latitude and longitude:
                dictionary.append({"latitude": latitude, "longitude": longitude, "permit":permit, "date":date}) #'name': name, 'type':type})
                #print(dictionary)
    
    # Process the start_date and end_date as needed for your API request
    # You can use the values in your API request to https://data.calgary.ca/resource/c2es-76ed.geojson

    # For demonstration, let's just return the selected date range
    #print(dictionary)
    print("Function has run")
    permit_data = dictionary
    return  render_template('search.html', permit_data = permit_data) #jsonify(dictionary)

if __name__ == '__main__':
    app.run(debug=True)


    #In order to run the code type python -m flask run in the command line
    # run this first at the beginning of the session  $env:FLASK_APP = "application.py"


