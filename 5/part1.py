rules_data, sequences_data = open("input").read().split("\n\n")

rules = [list(map(int, rule.split("|"))) for rule in rules_data.split("\n")]
sequences = [list(map(int, sequence.split(","))) for sequence in sequences_data.split("\n") if sequence]

def satisfies_rules(sequence):
    positions = {val: i for i, val in enumerate(sequence)}

    for a, b in rules:
        if a not in positions or b not in positions:
            continue

        if positions[a] > positions[b]:
            return False
        
    return True

res = 0
for sequence in sequences:
    if satisfies_rules(sequence):
        res += sequence[len(sequence)//2]

print(res)
