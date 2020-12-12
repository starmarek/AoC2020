with open("input.txt", "r") as f:
    data = [item for item in f.read().splitlines()]

valid_pass_count_1_star = 0
valid_pass_count_2_star = 0
for expr in data:
    splitted = expr.split(":")

    password = splitted[1].lstrip()
    letter = splitted[0][-1]
    (lower, upper) = splitted[0][:-1].strip().split("-")

    if int(lower) <= password.count(letter) <= int(upper):
        valid_pass_count_1_star += 1

    if (
        password[int(lower) - 1] == letter
        and not password[int(upper) - 1] == letter
        or not password[int(lower) - 1] == letter
        and password[int(upper) - 1] == letter
    ):
        valid_pass_count_2_star += 1

print(valid_pass_count_1_star, valid_pass_count_2_star)
