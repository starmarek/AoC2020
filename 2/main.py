with open("input.txt", "r") as f:
    data = [item for item in f.read().splitlines()]

valid_pass_count = 0
for expr in data:
    splitted = expr.split(":")

    password = splitted[1].lstrip()
    letter = splitted[0][-1]
    (lower, upper) = splitted[0][:-1].strip().split("-")

    if int(lower) <= password.count(letter) <= int(upper):
        valid_pass_count += 1

print(valid_pass_count)
