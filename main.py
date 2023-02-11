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
    return graph_data


def prompt_user(cities: dict[str, (float, float)]):
    while True:
        start = random.choice(list(cities))
        destination = random.choice(list(cities))
        while start == destination:
            destination = random.choice(list(cities))
        start_coords: (float, float) = input(f"Please enter the coordinates for {start} in the format (x, y): ")
        end_coords: (float, float) = input(f"Please enter the coordinates for {destination} in the format (x, y): ")
        if start_coords == cities[start] and end_coords == cities[destination]:
            distance = (abs(start[0] - destination[0])**2 + abs(start[0] - destination[1])**2)**0.5
            print(f"The shortest distance between {start} and {destination} is {distance}")
            break
        


print(load_data("cities_coords.txt"))
prompt_user(load_data("cities_coords.txt"))


# References:
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
