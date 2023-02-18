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


def find_shortest_path(start: str) -> (dict[str, str], dict[str, float]):
    global current_node, current_index
    edges_dict: dict[(str, str), float] = load_edges("cities_coords.txt", "cities_graph.txt")
    graph: list[(str, list[str])] = load_graph("cities_graph.txt")
    unvisited = [c for c, _ in graph]
    shortest_path: dict[str, float] = {}
    prev_cities: dict[str, str] = {}
    max_val = sys.maxsize
    for node in unvisited:
        shortest_path[node] = max_val
    shortest_path[start] = 0
    while unvisited:
        current_node = None
        for node in unvisited:
            if current_node is None:
                current_node = node
            elif shortest_path[node] < shortest_path[current_node]:
                current_node = node
        for c, es in graph:
            if c == current_node:
                neighbours = es
                break
        for neighbour in neighbours:
            tentative = shortest_path[current_node] + edges_dict[(current_node, neighbour)]
            if tentative < shortest_path[neighbour]:
                shortest_path[neighbour] = tentative
                prev_cities[neighbour] = current_node
        unvisited.remove(current_node)
    return prev_cities, shortest_path


def print_result(prev_cities: dict[str, str], shortest_path: dict[str, float], start_node: str, target_node: str):
    path: list[str] = []
    node: str = target_node
    while node != start_node:
        path.append(node)
        node = prev_cities[node]
    path.append(start_node)
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


def run():
    prev_cities, shortest_path = find_shortest_path("Ankara")
    print_result(prev_cities, shortest_path, "Ankara", "Moscow")


run()

if __name__ == "__main__":
    pass

# References:
# https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
