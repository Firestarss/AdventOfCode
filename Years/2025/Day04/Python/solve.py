import time


input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines_d = dict()
    lines =  [a.strip() for a in f.readlines()]
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "@":
                lines_d[(x,y)] = lines[y][x]


def part1():
    out = 0
    for point in lines_d:
        neighbors = 0
        for coord in [(1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1)]:
            tmp_coord = (point[0] + coord[0], point[1] + coord[1])
            if tmp_coord in lines_d:
                neighbors += 1

        if neighbors < 4:
            out += 1

    print(out)

def part2():
    running = True
    out = 0
    while running:
        running = False
        to_del = set()
        for point in lines_d:
            if lines_d[point] == ".": continue
            neighbors = 0
            for coord in [(1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1)]:
                tmp_coord = (point[0] + coord[0], point[1] + coord[1])
                if tmp_coord in lines_d:
                    neighbors += 1

            if neighbors < 4:
                out += 1
                running = True
                to_del.add(point)

        for roll in to_del:
            del lines_d[roll]

    print(out)

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
