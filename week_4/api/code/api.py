from flask import Flask, request 

import os
import json
import random

app = Flask(__name__)

@app.route('/meal_rec')

def meal_pick():
  
    meals = [
    {'Meal': 'DOUBLE-DOUBLE',
     'Price': '$8'},
    {'Meal': 'CHEESEBURGER',
     'Price': '$7'},
    {'Meal': 'HAMBURGER',
     'Price': '$6'},
    {'Meal': 'FRENCH-FRIES',
     'Price': '$5'},
    {'Meal': 'DIET-COKE',
     'Price': '$3'},
    {'Meal': 'DOUBLE-DOUBLE-Combo',
     'Price': '$10'},
    {'Meal': 'CHEESEBURGER-Combo',
     'Price': '$9'},
    {'Meal': 'HAMBURGER-Combo',
     'Price': '$8'},
    {'Meal': 'FRENCH-FRIES-Combo',
     'Price': '$6'},
   {'Meal': 'HAPPY-MEAL-1',
     'Price': '$11'},
   {'Meal': 'HAPPY-MEAL-2',
     'Price': '$12'},
   {'Meal': 'HAPPY-MEAL-3',
     'Price': '$13'},
   {'Meal': 'HAPPY-MEAL-4',
     'Price': '$14'},
   {'Meal': 'HAPPY-MEAL-5',
     'Price': '$15'},
    {'Meal': 'HAPPYE-MEAL-6',
     'Price': '$16'},]

    random_meal = random.choice(meals)
    return json.dumps(random_meal)

if __name__ == '__main__':
    app.run(host="0.0.0.0")