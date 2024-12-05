file = open('input.txt', 'r')

input = file.read().splitlines()

def solve1():
    half_safe_reports = []
    safe_reports = []

    for el in input:
        levels = list(map(int, el.split()))
        increasing = all(i < j for i, j in zip(levels, levels[1:]))
        decreasing = all(i > j for i, j in zip(levels, levels[1:]))

        if increasing or decreasing:
            half_safe_reports.append(levels)

    for report in half_safe_reports:
        skip_report = False
        for x, y in zip(report, report[1:]):
            if abs(x - y) > 3:
                skip_report = True
                break

        if skip_report:
            continue

        safe_reports.append(report)

    print(len(safe_reports))

def main():
    solve1()

main()