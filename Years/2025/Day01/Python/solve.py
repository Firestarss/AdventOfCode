import time

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [(a.strip()[0], int(a.strip()[1:])) for a in f.readlines()]

def part1():
    current = 50
    out_count = 0
    for dir, num in lines:
        if dir == "L":
            current = (current - num) % 100
        elif dir == "R":
            current = (current + num) % 100

        if current == 0:
            out_count += 1

    print(out_count)

def part2():
    current = 50
    out_count = 0
    for dir, num in lines:
        for _ in range(num):
            if dir == "L":
                current = (current - 1) % 100
            elif dir == "R":
                current = (current + 1) % 100
            
            if current == 0:
                out_count += 1

    print(out_count)

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
