import random
from time import time


def load_coordinates(coord_file: str) -> list[(float, float)]:
    result: list[(float, float)] = []
    with open(coord_file, "r") as reader:
        for line in reader.readlines():
            line = line.strip()
            connection = line.split(",")
            result.append((float(connection[1]), float(connection[2])))
    return result


def load_graph():
    pass


if __name__ == "__main__":
    pass

# References:
# Lect%2002.pdf
