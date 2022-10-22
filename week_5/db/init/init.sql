
CREATE TABLE IF NOT EXISTS meal (
    Meal_ID SERIAL PRIMARY KEY,
    Meal_Name TEXT NOT NULL,
    Meal_Price INTEGER NOT NULL
);

INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('DOUBLE-DOUBLE', 1);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('CHEESEBURGER', 2);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAMBURGER', 3);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('FRENCH-FRIES', 4);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('DIET-COKE', 5);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('DOUBLE-DOUBLE-Combo', 6);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('CHEESEBURGER-Combo', 7);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAMBURGER-Combo', 8);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('FRENCH-FRIES-Combo', 9);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAPPY-MEAL-1', 10);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAPPY-MEAL-2', 11);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAPPY-MEAL-3', 12);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAPPY-MEAL-4', 13);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAPPY-MEAL-5', 14);
INSERT INTO meal(Meal_Name, Meal_Price) VALUES ('HAPPYE-MEAL-6', 15);