from functools import reduce

reports = [list(map(int, line.split())) for line in open('input').readlines()]

def levels_diff(levels):
    return [levels[i] - levels[i-1] for i in range(1, len(levels))]

def is_safe(report):
    diff = levels_diff(report)
    min_diff = min(diff)
    max_diff = max(diff)

    if min_diff >= 1 and max_diff <= 3:
        return True
    
    return min_diff >= -3 and max_diff <= -1

def is_safe_with_tolerance(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False
    

print(reduce(lambda acc, report: acc + is_safe_with_tolerance(report), reports, 0))