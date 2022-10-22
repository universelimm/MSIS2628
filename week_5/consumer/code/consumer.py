from flask import Flask, render_template
import requests
import os
import json
from urllib.request import urlopen 
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def get_meal():

   response = requests.get('http://' + str(os.environ.get("API_HOST")) + ':' + str(os.environ.get("API_PORT")) + "/" + str(os.environ.get("API_ENDPOINT")))
   response = response.content
   response = json.loads(response)
   meal = response['Meal']
   price = response['Price']

   return render_template('index.html', meal = meal, price = price)

app.run(host='0.0.0.0', port = 81)