import re
from functools import cache

looking_for = "shiny gold"
found = 0
with open("input.txt") as f:
    data = dict(
        re.sub(r"\d", "", re.sub(r"\sbag[s]?", "", line)).split(" contain ")
        for line in f.read().splitlines()
    )
    data = {key: val.strip(" .").split(",  ") for key, val in data.items()}

@cache
def check_bag(bag):
    if looking_for in bag:
        return True
    if "no other" in bag:
        return False
    for inner_bag in data[bag]:
        if check_bag(inner_bag):
            return True
        
for inner_bags in data.values():
    for bag in inner_bags:
        if check_bag(bag):
            found += 1
            break

print(found)
