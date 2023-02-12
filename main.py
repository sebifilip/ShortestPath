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


print(load_coordinates("cities_coords.txt"))
print(load_graph("cities_graph.txt"))


if __name__ == "__main__":
    pass

# References:
# Lect%2002.pdf
