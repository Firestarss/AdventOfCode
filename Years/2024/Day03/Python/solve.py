import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
    line = "".join(lines)

def part1():
    muls = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
    muls = [list(map(int,re.findall('\d+', mul))) for mul in muls]
    muls = [mul[0] * mul[1] for mul in muls]

    print(sum(muls))

def part2():
    output = []

    tokens = re.findall('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)

    to_add = True
    for token in tokens:
        if token == "do()":
            to_add = True
        elif token == "don't()":
            to_add = False
        elif to_add:
            muls = list(map(int,re.findall('\d+', token)))
            output.append(muls[0] * muls[1])

    print(sum(output))

part1()
part2()