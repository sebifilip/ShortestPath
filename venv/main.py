import random

def load_data(data: str):
    graph_data = {}
    cities = []
    with open(data, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            connection = line.split()
            graph_data[connection[0], connection[1]] = int(connection[2])
            graph_data[connection[1], connection[0]] = int(connection[2])
            pair = [connection[0], connection[1]]
            for c in pair:
                if c not in cities:
                    cities.append(c)

    print(cities)
    print(graph_data)
    gen_matrix(graph_data, cities)


def gen_matrix(graph_data: dict[list[(str, str)], int], cities: list[str]):
    distance_matrix = {}
    for c in sorted(cities):
        distance_matrix[c] = []
    for c1 in distance_matrix:
        for c2 in sorted(cities):
            if c1 != c2 and (c1, c2) in list(graph_data):
                distance_matrix[c1].append(graph_data[(c1, c2)])
            else:
                distance_matrix[c1].append(0)
    print(distance_matrix)


def find_shortest_path(start, end):
    shortest_paths = []


def prompt_user(graph_data: dict[list[(str, str)], int], cities: list[str]):
    start = random.choice(list(cities))
    destination = random.choice(list(cities))
    while start == destination:
        destination = random.choice(list(cities))
    shortest_path = int(input(f"Find the shortest path between {start} and {destination}: "))


print(load_data("cities_graph"))
