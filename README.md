# SmartBite

**Smart Fast-Food Nutrition, Budget & Meal Finder**

## About the Project

SmartBite is a command-line food recommendation and ordering system developed using Python.

It helps users find fast-food options based on their preferred:

* Maximum calorie limit
* Minimum protein requirement
* Maximum budget
* Brand
* Food category
* Food preference mode

The system also allows users to compare foods, add items to a cart, manage quantities, and complete a simulated checkout.

## Features

* User registration and login
* Guest mode
* Food recommendations based on user requirements
* Calorie, protein, and budget filtering
* Brand and category filtering
* Different recommendation modes:

  * Cheat Meal
  * High Protein
  * Low Calorie
  * Best Value
* Food ranking using a recommendation score
* Closest alternatives when no exact match is found
* Food comparison
* Shopping cart
* Multiple quantities for the same food
* Partial quantity removal
* Cart total calculation
* Simulated payment options
* Order confirmation

## Project Structure

```text
SmartBite/
│
├── main.py
├── food_data.py
├── validation.py
├── filters.py
├── recommender.py
├── comparison.py
├── cart.py
├── user.py
├── .gitignore
└── README.md
```

## Technologies Used

* Python
* Python dictionaries and lists
* Functions
* Conditional statements
* Loops
* Exception handling
* Modular programming

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your system.

### 2. Open the Project

Open the SmartBite project folder in VS Code or another Python-supported editor.

### 3. Run the Program

Open a terminal inside the project folder and run:

```bash
python main.py
```

### 4. Start Using SmartBite

You can:

1. Login
2. Register a new user
3. Continue as a guest

Then use the main menu to find recommendations, manage your cart, or checkout.

## Food Data

The project currently uses a small built-in food dataset for demonstration purposes.

The calorie, protein, and price values are **illustrative/sample values** and should not be treated as exact nutritional or medical information.

## Project Purpose

The purpose of SmartBite is to demonstrate how Python programming concepts can be used to create a practical command-line application.

The project combines data handling, filtering, recommendation logic, user input validation, comparison, cart management, and basic checkout functionality into one application.

## Limitations

* The application runs through the command line and does not have a graphical user interface.
* User accounts are stored only while the program is running.
* Payment is simulated and no real transaction takes place.
* Food data is stored locally in the Python program.
* Nutritional and price values are sample values.

## Future Improvements

Possible future improvements include:

* Adding a larger food database
* Storing user accounts permanently
* Adding a graphical or web interface
* Connecting to live restaurant and food data
* Adding more advanced recommendation methods
* Adding order history

## Disclaimer

SmartBite is an academic project created for demonstration and educational purposes. The nutritional and price information used in the application is illustrative and may not represent current or exact real-world values.
