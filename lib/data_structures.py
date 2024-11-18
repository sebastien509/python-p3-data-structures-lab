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
    return spicy_foods[0][0], spicy_foods[1][0], spicy_foods[2][0]

def get_spiciest_foods(spicy_foods):
    return spicy_foods[0]

def print_spicy_foods(spicy_foods):
    return print(spicy_foods[0])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    return cuisine[0][1],spicy_foods[1][1], spicy_foods[2][1]

def print_spiciest_foods(spicy_foods):
    return spicy_foods[0][0], spicy_foods[2][0]

def get_average_heat_level(spicy_foods):
    return spicy_foods[2][2]

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food = {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}
    
    return spicy_foods.append(spicy_food)



    # spicy_foods[3].name = "Griot Pikliz"
    # spicy_foods[3].cuisine = "Haitien"
    # spicy_foods[3].heat_level = 8