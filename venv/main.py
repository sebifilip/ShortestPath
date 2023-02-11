import random

def load_data(data: str):
    graph_data = {}
    with open(data, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            connection = line.split()
            graph_data[connection[0], connection[1]] = int(connection[2])
    return graph_data


def shortest_path(cities: dict[list[str], int]):
    start = random.choice(list(cities))
    destination = random.choice(list(cities))
    while start == destination:
        destination = random.choice(list(cities))
    shortest_path = int(input(f"Find the shortest path between {cities[0]} and {cities[1]}: "))

print(load_data("cities_graph"))
