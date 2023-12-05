lines = [line.strip() for line in list(open("input3.txt", "r").readlines())]
print(lines)


def is_star(char):
    return char == "*"


hashmap = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        hashmap[(i, j)] = char

print(hashmap)


def h_default(place):
    if not place in hashmap:
        return False
    return is_star(hashmap[place])


start = 0
stop = 0


count = 0
line = 0
answers = []
while True:
    try:
        value = hashmap[(line, start)]
    except KeyError:
        line += 1
        if len(lines) <= line:
            break
        start = 0
        stop = 0
        value = hashmap[(line, start)]
    if value.isdigit():
        stop = start
        yeah = False
        gear_address = None
        while (line, stop) in hashmap and hashmap[(line, stop)].isdigit():
            # stop checks the values here
            left = (line, stop - 1)
            right = (line, stop + 1)
            top = (line - 1, stop)
            bottom = (line + 1, stop)
            top_left = (line - 1, stop - 1)
            top_right = (line - 1, stop + 1)
            bottom_left = (line + 1, stop - 1)
            bottom_right = (line + 1, stop + 1)
            for place in [
                left,
                right,
                top,
                bottom,
                top_left,
                top_right,
                bottom_left,
                bottom_right,
            ]:
                try:
                    if h_default(place):
                        yeah = True
                        gear_address = place
                        print("deneme", start, stop)
                except KeyError:
                    print("HEYY")
                    yeah = False
                    pass
            stop += 1
        number = ""
        for i in range(start, stop):
            number += hashmap[(line, i)]
        print(
            "numero:",
            number,
            "line:",
            line,
            "start:",
            start,
            "stop:",
            stop,
            "VALID:",
            yeah,
        )
        if yeah:
            answers.append(
                {
                    "number": number,
                    "gear_address": gear_address,
                    "line": line,
                    "start": start,
                    "stop": stop,
                }
            )
            gear_address = None
            count += int(number)
        start = stop
    start += 1

print(answers)

ans = 0
for i in answers:
    for j in answers:
        if i == j:
            continue
        if i["gear_address"] == j["gear_address"]:
            print(i, j)
            ans += int(i["number"]) * int(j["number"])

print(ans)
print(ans / 2)
