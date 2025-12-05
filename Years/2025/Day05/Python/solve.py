import time


input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    rules, values = f.read().strip().split("\n\n")
    rules = rules.strip().split("\n")
    rules = [(int(a[0]), int(a[1])) for a in [b.split("-") for b in rules]]
    rules = sorted(rules)
    values = [int(a) for a in values.strip().split("\n")]

def part1():
    output = 0

    for value in values:
        for rule in rules:
            if rule[0] <= value <= rule[1]:
                output += 1
                break

    print(output)

def part2():
    new_rules = [list(rules[0])]
    for rule in rules:
        lb, ub = rule
        nlb, nub = new_rules[-1]

        if lb <= nub:
            new_rules[-1][1] = max(nub, ub)
        else:
            new_rules.append(list(rule))

    print(sum([rule[1] - rule[0] + 1 for rule in new_rules]))

    # 432702314623892 too high
    # 334427811476227 too low

def main():
    overall_start = time.perf_counter()
    p1_start = time.perf_counter()

    print("Part 1:")
    part1()

    p1_end = time.perf_counter()
    p2_start = time.perf_counter()

    print("\nPart 2:")
    part2()

    p2_end = time.perf_counter()
    overall_end = time.perf_counter()

    print("\nRuntimes in seconds:")
    print(f"    Total  : {overall_end - overall_start:.2f}")
    print(f"    Part 1 : {p1_end - p1_start:.2f}")
    print(f"    Part 2 : {p2_end - p2_start:.2f}")

main()
