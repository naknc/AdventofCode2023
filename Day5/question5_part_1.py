import time


def parser():
    f = open("input5.txt", "r")
    all_file = f.read()
    all_file = all_file.split("\n\n")
    seed_info = all_file[0]
    seed_info = seed_info.strip().split(" ")[1:]
    seed_info = [int(s) for s in seed_info]
    all_file = all_file[1:]
    all_rules = []
    for rules in all_file:
        lines = rules.split("\n")
        lines = lines[1:]
        lines = [line.strip().split(" ") for line in lines]
        lines = [[int(number) for number in line] for line in lines]
        all_rules.append(lines)
    return (all_rules, seed_info)


def mapper(seed, rules):
    if len(rules) == 0:
        return seed

    def source_check(s, rule):
        _destination, source, step = rule
        if s >= source and s < source + step:
            return True
        return False

    if source_check(seed, rules[0]):
        destination, source, _step = rules[0]
        new_seed = destination - (source - seed)
        return new_seed
    return mapper(seed, rules[1:])


answers = -1
all_rules, seed_info = parser()
before = time.perf_counter()

for seed in seed_info:
    for rules in all_rules:
        seed = mapper(seed, rules)

    if answers > seed or answers == -1:
        answers = seed
print(answers)
print(f"Time: {time.perf_counter() - before:.6f} seconds")
