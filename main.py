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
    """
    This search page is the same as the index page, it just has the functionality of the api

    I connect to the api, and then iterate through the different dictionaries to get all of the necessary information.
    """
    dictionary = []
    start_date = str(request.form['start_date'])
    end_date = str(request.form['end_date'])

    api_url = "https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate>'%s'and issueddate<'%s'" %(start_date, end_date)
    res = requests.get(api_url)
    
    info = res.json()
    if 'features' in info and info['features']:
        for item in info['features']:

            data = item['geometry']

            latitude = round(data.get('coordinates')[0], 4)
            print(latitude)
            longitude = round(data.get('coordinates')[1], 4)
            data1 = item['properties']
            permit = str(data1.get('permitnum'))
            date = str(data1.get('issueddate'))
            name = data1.get('contractorname')
            com = data1.get('communityname')
            work = data1.get('workclassgroup')
            org = data1.get('originaladdress')
            type = data1.get('permittype')
            if latitude and longitude:
                dictionary.append({"latitude": latitude, "longitude": longitude, "permit_number":permit, "date":date, 'name': name, 'type':type, 'com':com, 'work':work, 'org':org})

    
    

  

    print("Function has run")
    permit_data = dictionary
    return  render_template('search.html', permit_data = permit_data) 

if __name__ == '__main__':
    app.run(debug=True)


    #In order to run the code type python -m flask run in the command line
    # run this first at the beginning of the session  $env:FLASK_APP = "application.py"


