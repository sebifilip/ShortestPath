import random
from cities_graph import map

def shortest_path(cities: dict[str, list[int]]):
    cities = []
    cities.append(random.choice(list(european_cities)))
    cities.append(random.choice(list(european_cities)))
    shortest_path = int(input(f"Find the shortest path between {cities[0]} and {cities[1]}: "))

european_cities = {
    "Amsterdam": [0, 3, 2, 0, 3, 0, 1, 0, 0, 0],
    "Berlin": [3, 0, 2, 0, 0, 0, 6, 12, 8],
    "Copenhagen": [2, 2, 0, 0, 0, 0, 0, 0, 0, 16],
    "Dublin": [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
    "London": [3, 0, 0, 5, 0, 0, 10, 30, 0, 0],
    "Madrid": [0, 0, 0, 0, 25, 0, 10, 0, 0, 0],
    "Paris": [1, 6, 0, 0, 10, 10, 0, 0, 12, 0],
    "Reyjjavik": [0, 0, 0, 0, 30, 0, 0, 0, 0, 0],
    "Rome": [0, 12, 0, 0, 0, 0, 12, 0, 0],
    "Warsaw": [0, 8, 16, 0, 0, 0, 0, 0, 0]
    }