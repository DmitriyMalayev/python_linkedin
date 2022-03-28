def main():
    x, y = 10, 100
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else:
        result = "x is greater than y"

    # print(result)


x, y = 10, 100

result = "x is less than y" if x < y else "x is greater or equal to y"
print(result)


# Match Case used to compare multiple values

value = "one"
match value:
    case "one":
        result = 1
    case "two":
        result = 2
    case "three" | "four":
        result = (3, 4)
    case _:
        result = -1  # default case handler, handles all other conditions
print(result)
