spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if ["heat_level"] >= 7 ]

def print_spicy_foods(spicy_foods):
    return [food for food in spicy_foods if ["heat_level"] >= 5] 

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [[cuisine] for food in spicy_foods if ["heat_level"] >= 5]

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods :
        heat_emoji = "🌶️" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")

def get_average_heat_level(spicy_foods):
    return [food for food in spicy_foods if 5 > ["heat_level"]< 7]

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}
    spicy_foods.append(spicy_food)



    # spicy_foods[3].name = "Griot Pikliz"
    # spicy_foods[3].cuisine = "Haitien"
    # spicy_foods[3].heat_level = 8