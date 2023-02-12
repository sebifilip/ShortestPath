import random
from time import time


def load_data(data: str):
    cities_data = {}
    i = 0
    with open(data, "r") as reader:
        for line in reader.readlines():
            if i > 0:
                line = line.strip()
                connection = line.split(",")
                cities_data[connection[0]] = (float(connection[1]), float(connection[2]))
            i += 1
    return cities_data


def prompt_user(cities: dict[str, (float, float)], start, destination):
    while True:
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


def test_run(start, end):
    start_time = time()
    cities_dict = load_data("cities_coords.txt")
    print(cities_dict)
    prompt_user(cities_dict, start, end)
    end_time = time()
    elapsed = end_time - start_time
    print(f"Elapsed time: {elapsed} seconds")


if __name__ == "__main__":
    test_run("Bucharest", "Zurich")
    test_run("London", "Astana")


# References:
# Lect%2002.pdf
