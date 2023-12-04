lines = [ line.strip() for line in list(open("input3.txt", "r").readlines())]
print(lines)
def is_symbol(char):
    if char == "." or char.isdigit():
        return False
    return True

hashmap = {}

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        hashmap[(i,j)] = char

print(hashmap)


def h_default(place):
    if not place in hashmap:
        return False
    return is_symbol(hashmap[place]) 

start = 0
stop = 0


count = 0
line = 0
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
        while (line, stop) in hashmap and hashmap[(line, stop)].isdigit():
            # stop checks the values here
            left = (line, stop - 1)
            right = (line, stop + 1 )
            top = (line - 1, stop)
            bottom = (line + 1, stop )
            top_left = (line-1, stop-1)
            top_right = (line-1, stop+1)
            bottom_left = (line+1, stop-1)
            bottom_right = (line+1, stop+1)
            for place in [left,right,top,bottom,top_left,top_right, bottom_left,bottom_right]:
                try:
                    if h_default(place):
                        yeah = True
                        print("deneme", start, stop)
                except KeyError:
                    print("HEYY")
                    yeah = False
                    pass 
            stop += 1
        number = ""
        for i in range(start, stop):
            number += hashmap[(line, i)]
        print("numero:",number, "line:",line, "start:", start,"stop:",stop , "VALID:", yeah)
        if yeah:
            count += int(number)
        start = stop
    start += 1

print(count)
    

