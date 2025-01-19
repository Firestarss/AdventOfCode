

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
    grid = dict()
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col in ".#":
                grid[(c,r)] = col
            else:
                grid[(c,r)] = "."
                guard = [col, (c,r)]
                start = (col, (c,r))

def is_loop(insertion):
    if insertion == start: return False


    guard = [start[0], start[1]]

    seen = set()
    turns = ["^", ">", "v", "<", "^"]
    dirs = {"^": (0,-1), ">": (1,0), "v": (0,1), "<": (-1,0)}

    while guard[1] in grid:
        if ((guard[0], guard[1])) in seen:
            return True
        seen.add((guard[0], guard[1]))
        next_pos = (guard[1][0] + dirs[guard[0]][0], guard[1][1] + dirs[guard[0]][1])
        if next_pos in grid and (grid[next_pos] == "#" or next_pos == insertion):
            guard[0] = turns[turns.index(guard[0]) + 1]
        else:
            guard[1] = next_pos


    return False


def part1():
    seen = set()
    turns = ["^", ">", "v", "<", "^"]
    dirs = {"^": (0,-1), ">": (1,0), "v": (0,1), "<": (-1,0)}

    while guard[1] in grid:
        seen.add(guard[1])
        next_pos = (guard[1][0] + dirs[guard[0]][0], guard[1][1] + dirs[guard[0]][1])
        if next_pos in grid and grid[next_pos] == "#":
            guard[0] = turns[turns.index(guard[0]) + 1]
        else:
            guard[1] = next_pos

    print(len(seen))

    path = seen
    print(sum([is_loop(cell) for cell in path]))

part1()