import time

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [list(map(int, a.strip().split('-'))) for a in f.read().split(',')]

def part1():
    out = 0
    for line in lines:
        for i in range(line[0], line[1] + 1):
            id = str(i)
            if id[len(id)//2:] == id[:len(id)//2]:
                out += i

    print(out)

def part2():
    output = 0

    for line in lines:
        for i in range(line[0], line[1] + 1):
            id = str(i)
            if id in (id + id)[1:-1]:
                output += i

    print(output)

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
