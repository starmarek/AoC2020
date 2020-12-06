from itertools import combinations
from math import prod


with open("input.txt", "r") as f:
    data = [int(item) for item in f.read().splitlines()]

    for pair in combinations(data, 2):
        if sum(pair) == 2020:
            print(prod(pair))
