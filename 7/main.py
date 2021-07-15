import re
import time

looking_for = "shiny gold"
found = 0
with open("input.txt", "r") as f:
    data = dict(
        re.sub(r"\d", "", re.sub(r"\sbag[s]?", "", line)).split(" contain ")
        for line in f.read().splitlines()
    )

def rec(val):
    global found
    if looking_for in val:
        found += 1
        return True
    if "no other" in val:
        return False
    for bag in val.strip(" .").split(",  "):
        if rec(data[bag]):
            return True
begin = time.time()    
for val in data.values():
    rec(val)
end = time.time()
print(found)
print(end-begin)
