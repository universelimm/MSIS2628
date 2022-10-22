from random import randint
from flask import Flask,request,jsonify
import json
import os
from sqlalchemy import create_engine

app = Flask(__name__)

db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('PG_USER')
db_pass = os.environ.get('PG_PASS')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('PG_PORT') 

url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

db = create_engine(url)

@app.route('/meal_rec')
@app.route('/')

def meal_pick():
    query = "SELECT Meal_Name,Meal_price FROM Meals ORDER BY RANDOM() LIMIT 1;"
    rows = db.execute(query)

    rowarray_list = []

    for row in rows:
        t = (row[0], row[1])
        rowarray_list.append(t)

    return list(rowarray_list)

def index():
    return jsonify(get_meal_records_from_db())

app.run(host='0.0.0.0', port=os.environ.get('API_PORT'))