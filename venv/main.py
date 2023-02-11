import random


def load_data(data: str):
    graph_data = {}
    i = 0
    with open(data, "r") as reader:
        for line in reader.readlines():
            if i > 0:
                line = line.strip()
                connection = line.split(",")
                graph_data[connection[0]] = (float(connection[1]), float(connection[2]))
            i += 1
    print(graph_data)


def prompt_user(cities: dict[list[(str, str)], int]):
    start = random.choice(list(cities))
    destination = random.choice(list(cities))
    while start == destination:
        destination = random.choice(list(cities))
    shortest_path = sqrt(abs(cities[start][0]^2) + abs(cities[start[1]^2])) + sqrt(abs(cities[destination][0]^2) + abs(cities[destination[1]^2]))
    shortest_input = int(input(f"Find the shortest path between {start} and {destination}: "))
    if shortest_input == shortest_path:
        print("Correct!")


print(load_data("cities_coords.txt"))


# References:
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
