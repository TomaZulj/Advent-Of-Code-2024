import re

file = open('input.txt', 'r')

input = file.read()
pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

def solve1():
    matches = re.findall(pattern, input)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])

    print(result)

def solve2():

    split_regex = re.split(r"(do\(\)|don't\(\))", input)
    findall = True
    result = 0

    for i in split_regex:
        if i == 'do()':
            findall = True
        elif i == "don't()":
            findall = False

        if findall:
            matches = re.findall(pattern, i)
            for match in matches:
                result += int(match[0]) * int(match[1])

    print(result)

def main():
    solve1()
    solve2()

main()