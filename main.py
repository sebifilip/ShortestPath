import random
from time import time


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
        start_x = float(input(f"Please enter the x coordinate for {start}: "))
        start_y = float(input(f"Please enter the y coordinate for {start}: "))
        end_x = float(input(f"Please enter the x coordinate for {destination}: "))
        end_y = float(input(f"Please enter the y coordinate for {destination}: "))
        start_coords = (start_x, start_y)
        end_coords = (end_x, end_y)
        if start_coords == cities[start] and end_coords == cities[destination]:
            distance = ((start_x - end_x)**2 + (start_y - end_y)**2)**0.5
            print(f"The shortest distance between {start} and {destination} is {distance}")
            break
        else:
            print("Incorrect cooridnates!")


def test_run():
    t1 = time()
    print(load_data("cities_coords.txt"))
    t2 = time()
    prompt_user(load_data("cities_coords.txt"))
    print(f"Time taken to open the file and get the shortest path between two cities is {t2 - t1} seconds")


if __name__ == "__main__":
    test_run()


print(load_data("cities_coords.txt"))
start_time = time()
prompt_user(load_data("cities_coords.txt"))
end_time = time()
elapsed = end_time - start_time
print(f"Elapsed time: {elapsed} seconds")


# References:
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
