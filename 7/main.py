import re

from anytree import LevelOrderIter, Node, RenderTree, cachedsearch

with open("input.txt", "r") as f:
    data = [
        re.sub(r"\d", "", re.sub(r"\sbag[s]?", "", line)).split(" contain ")
        for line in f.read().splitlines()
    ]

# build tree
master = Node("master")
for rule in data:
    master_rule = Node(rule[0], parent=master)
    for slave_rule in rule[1].split(","):
        Node(slave_rule.strip(" ."), parent=master_rule)


def fill_node(node):
    new_children = []
    for children in node.children:
        print(node.children)
        found_node = cachedsearch.find_by_attr(master, children.name, maxlevel=2)
        print(found_node.name)
        new_children.append(found_node)
        if found_node.name != "no other":
            fill_node(found_node)
    node.children = new_children


# fill the tree
for node in LevelOrderIter(master, maxlevel=2):
    if node.name == "master":
        continue
    fill_node(node)

for pre, fill, node in RenderTree(master):
    print("%s%s" % (pre, node.name))
