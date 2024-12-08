rules_data, sequences_data = open("input").read().split("\n\n")

rules = [list(map(int, rule.split("|"))) for rule in rules_data.split("\n")]
sequences = [list(map(int, sequence.split(","))) for sequence in sequences_data.split("\n") if sequence]

must_before = {}
for a, b in rules:
    if b not in must_before:
        must_before[b] = set()
    must_before[b].add(a)

def satisfies_rules(sequence):
    positions = {val: i for i, val in enumerate(sequence)}

    for a, b in rules:
        if a not in positions or b not in positions:
            continue

        if positions[a] > positions[b]:
            return False
        
    return True

def fix_sequence(sequence):
    seq = []

    remaining = set(sequence)
    candidate = sequence[0]
    while remaining:
        options = remaining.intersection(must_before.get(candidate, set()))
        if options:
            candidate = options.pop()
            continue

        seq.append(candidate)
        remaining.remove(candidate)
        if remaining:
            candidate = remaining.pop()
            remaining.add(candidate)

    return seq

res = 0
for sequence in sequences:
    if not satisfies_rules(sequence):
        sequence = fix_sequence(sequence)
        res += sequence[len(sequence)//2]

print(res)
