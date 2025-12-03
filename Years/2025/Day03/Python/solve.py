import time
import itertools

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [[int(b) for b in a.strip()] for a in f.readlines()]

def part1():
    print(sum([get_largest(line, 2) for line in lines]))

def part2():
    print(sum([get_largest(line, 12) for line in lines]))

def get_largest(bank, digits):
    can_remove = len(bank) - digits
    stack = []

    for batt in bank:
        while can_remove and stack and stack[-1] < batt:
            stack.pop()
            can_remove -= 1
        stack.append(batt)

    return int("".join(str(x) for x in stack[:digits]))


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
