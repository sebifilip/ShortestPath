import random

def load_data(data: str):
    graph_data = {}
    cities = []
    with open(data, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            connection = line.split()
            graph_data[connection[0], connection[1]] = int(connection[2])
            pair = [connection[0], connection[1]]
            for c in pair:
                if c not in cities:
                    cities.append(c)
    print(cities)
    print(graph_data)
    shortest_path(graph_data, cities)


def shortest_path(graph_data: dict[list[str], int], cities: list[str]):
    start = random.choice(list(cities))
    destination = random.choice(list(cities))
    while start == destination:
        destination = random.choice(list(cities))
    shortest_path = int(input(f"Find the shortest path between {start} and {destination}: "))


print(load_data("cities_graph"))
