import random
from time import time


def load_coordinates(coord_file: str) -> list[(float, float)]:
    result: list[(float, float)] = []
    with open(coord_file, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            coordinate = line.split(",")
            result.append((float(coordinate[0]), float(coordinate[1])))
    return result


def load_graph(graph_file: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    with open(graph_file, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            connection = line.split("->")
            edges = connection[1].split(",")
            result[connection[0]] = edges
    return result


def load_distances(c: str, g: str):
    coords = load_coordinates(c)
    graph = load_graph(g)
    cities_coords: dict[str, (float, float)] = {}
    distances: dict[(str, str), float] = {}
    for i in range(0, len(coords)):
        cities_coords[list(graph)[i]] = coords[i]
    for c1 in graph:
        for c2 in graph[c1]:
            distances[(c1, c2)] = 0
    for pair in distances:
        distances[pair] = ((cities_coords[pair[0][0]] + cities_coords[pair[0][1]])**2 + (cities_coords[pair[1][0]] + cities_coords[pair[1][1]])**2)**0.5
    return distances


def get_shortest_distance(cities_graph, start, destination):
    connections = [start]


print(load_distances("cities_coords.txt", "cities_graph.txt"))


if __name__ == "__main__":
    pass

# References:
# Lect%2002.pdf
