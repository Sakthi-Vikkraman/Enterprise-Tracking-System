import json
import random
from datetime import datetime, timedelta

categories = {
    "Food": 30,
    "Travel": 20,
    "Shopping": 15,
    "Bills": 20,
    "Health": 5,
    "Entertainment": 10
}

descriptions = {
    "Food": [
        "Swiggy order", "Zomato dinner", "Restaurant lunch",
        "Cafe coffee", "Office snacks"
    ],
    "Travel": [
        "Uber ride", "Metro recharge", "Petrol refill",
        "Auto fare", "Bus ticket"
    ],
    "Shopping": [
        "Amazon order", "Flipkart purchase", "Clothing store",
        "Electronics purchase", "Grocery shopping"
    ],
    "Bills": [
        "Electricity bill", "Internet bill", "Mobile recharge",
        "Water bill", "Gas cylinder"
    ],
    "Health": [
        "Pharmacy medicines", "Doctor consultation",
        "Health checkup", "Dental visit"
    ],
    "Entertainment": [
        "Movie ticket", "Netflix subscription",
        "Game purchase", "Concert ticket"
    ]
}

def weighted_category_choice():
    population = list(categories.keys())
    weights = list(categories.values())
    return random.choices(population, weights=weights, k=1)[0]

def random_amount(category):
    ranges = {
        "Food": (100, 800),
        "Travel": (50, 1500),
        "Shopping": (500, 5000),
        "Bills": (500, 4000),
        "Health": (300, 3000),
        "Entertainment": (200, 2000)
    }
    low, high = ranges[category]
    return round(random.uniform(low, high), 2)


expenses = []

for i in range(500):
    category = weighted_category_choice()

    expense = {
        "amount": random_amount(category),
        "category": category,
        "description": random.choice(descriptions[category]),
    }

    expenses.append(expense)

with open("expenses.json", "w") as f:
    json.dump(expenses, f, indent=2)

print("expenses.json generated with 500 realistic expenses")
