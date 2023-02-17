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


def load_graph(graph_file: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    with open(graph_file, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            connection = line.split("->")
            edges = connection[1].split(",")
            result[connection[0]] = edges
    return result


def load_distances(c: str, g: str) -> dict[(str, str), float]:
    coords: list[(float, float)] = load_coordinates(c)
    graph: dict[str, list[str]] = load_graph(g)
    cities_coords: dict[str, (float, float)] = {}
    distances: dict[(str, str), float] = {}
    for i in range(0, len(coords)):
        cities_coords[list(graph)[i]] = coords[i]
    for c1 in graph:
        for c2 in graph[c1]:
            distances[(c1, c2)] = 0
    for (c1, c2) in distances:
        distances[(c1, c2)] = ((cities_coords[c1][0] - cities_coords[c2][0])**2 + (cities_coords[c1][1] - cities_coords[c2][1])**2)**0.5
    return distances


def visit():
    global visited_and_distance
    v = -10
    for i in range(len(vertices)):
        if visited_and_distance[i][0] == 0 and (v < 0 or visited_and_distance[i][1] <= visited_and_distance[v][1]):
            v = i
    return v


edges_dict: dict[(str, str), float] = load_distances("cities_coords.txt", "cities_graph.txt")
graph_dict: dict[str, list[str]] = load_graph("cities_graph.txt")

# creating vertices
vertices: list[list[int]] = []
for city in graph_dict:
    vertices.append([])
for i in range(0, len(vertices)):
    v1 = list(graph_dict)[i]
    for j in range(0, len(vertices)):
        v2 = list(graph_dict)[j]
        if (v1, v2) in edges_dict:
            vertices[i].append(1)
        else:
            vertices[i].append(0)
print(vertices)

# creating edges
edges: list[list[float]] = []
for city in graph_dict:
    edges.append([])
for i in range(0, len(edges)):
    v1 = list(graph_dict)[i]
    for j in range(0, len(edges)):
        v2 = list(graph_dict)[j]
        if (v1, v2) in edges_dict:
            edges[i].append(edges_dict[(v1, v2)])
        else:
            edges[i].append(0)
print(edges)

num_of_vertices = len(vertices[0])

visited_and_distance: list[list[int]] = [[0, 0]]
for i in range(num_of_vertices - 1):
    visited_and_distance.append([0, sys.maxsize])

for vertex in range(0, num_of_vertices):
    to_visit = visit()
    for neighbour in range(num_of_vertices):
        if vertices[to_visit][neighbour] == 1 and visited_and_distance[neighbour][0] == 0:
            new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbour]
            if visited_and_distance[neighbour][1] > new_distance:
                visited_and_distance[neighbour][1] = new_distance

        visited_and_distance[to_visit][0] = 1

i = 0

# Printing the distance
for distance in visited_and_distance:
    print("Distance of ", chr(ord('a') + i),
          " from source vertex: ", distance[1])
    i = i + 1

print(load_distances("cities_coords.txt", "cities_graph.txt"))


if __name__ == "__main__":
    pass

# References:
# https://www.programiz.com/dsa/dijkstra-algorithm