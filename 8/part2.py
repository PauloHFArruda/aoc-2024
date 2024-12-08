import sys
from collections import defaultdict

antennas_map = open(sys.argv[1]).read().strip().split("\n")

antennas_pos_by_freq = defaultdict(list)

for i, row in enumerate(antennas_map):
    for j, cell in enumerate(row):
        if cell != ".":
            antennas_pos_by_freq[cell].append((i, j))

antennas_pairs = []

for positions in antennas_pos_by_freq.values():
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i + 1 :]:
            antennas_pairs.append((pos1, pos2))

count = 0

for i, row in enumerate(antennas_map):
    for j, cell in enumerate(row):
        if cell != ".":
            count += 1
            continue

        for ((a,b), (c,d)) in antennas_pairs:
            if (i-a)*(b-d) == (j-b)*(a-c):
                count += 1
                break

print(count)
