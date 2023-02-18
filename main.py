from time import time
import sys


def load_coordinates(coord_file: str) -> list[(float, float)]:
    result: list[(float, float)] = []
    with open(coord_file, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            coordinate = line.split(",")
            result.append((float(coordinate[0]), float(coordinate[1])))
    return result


def load_graph(graph_file: str) -> list[(str, list[str])]:
    result: list[(str, list[str])] = []
    with open(graph_file, "r") as reader:
        for line in reader.readlines():
            s_line: str = line.strip()
            connection = s_line.split("->")
            edge_list: list[str] = connection[1].split(",")
            result.append((connection[0], edge_list))
    return result


def load_edges(coord_file: str, graph_file: str) -> dict[(str, str), float]:
    coords: list[(float, float)] = load_coordinates(coord_file)
    graph: list[(str, list[str])] = load_graph(graph_file)
    cities_coords: dict[str, (float, float)] = {}
    distances: dict[(str, str), float] = {}
    for i in range(0, len(coords)):
        cities_coords[graph[i][0]] = coords[i]
    for city1, edge_list in graph:
        for city2 in edge_list:
            distances[(city1, city2)] = 0
    for (city1, city2) in distances:
        distances[(city1, city2)] = ((cities_coords[city1][0] - cities_coords[city2][0]) ** 2 +
                                     (cities_coords[city1][1] - cities_coords[city2][1]) ** 2) ** 0.5
    return distances


def load_vertices(graph_file: str) -> list[str]:
    vertex_list: list[str] = []
    graph: list[(str, list[str])] = load_graph(graph_file)
    for city1 in graph:
        vertex_list.append(city1[0])
    return vertex_list


def find_shortest_path(start, end):
    global current_node, current_index
    edges_dict: dict[(str, str), float] = load_edges("cities_coords.txt", "cities_graph.txt")
    graph: list[(str, list[str])] = load_graph("cities_graph.txt")
    unvisited = [c for c, _ in graph]
    shortest_path = {}
    prev_cities = {}
    max_val = sys.maxsize
    for city in unvisited:
        shortest_path[city] = max_val
    shortest_path[start] = 0
    while unvisited:
        current_node = None
        for node in unvisited:
            if current_node is None:
                current_node = node
            elif shortest_path[node] < shortest_path[current_node]:
                current_node = node
    for i in range(0, len(graph)):
        if graph[i][0] == current_node:
            current_index = i
    neighbours = graph[current_index][1]
    for n in neighbours:
        tentative = shortest_path[current_node] + edges_dict[(current_node, n)]
        if tentative < shortest_path[n]:
            shortest_path[n] = tentative
            prev_cities[n] = current_node
    unvisited.remove(current_node)
    return prev_cities, shortest_path

def run():
    start = input("Please enter a city to start: ")
    destination = input("Please enter a destination:")
    print(find_shortest_path(start, destination))

if __name__ == "__main__":
    pass

# References:
# https://www.programiz.com/dsa/dijkstra-algorithm
# https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
