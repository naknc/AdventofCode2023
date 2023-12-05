import re

lines = [ line.strip() for line in list(open("input4.txt", "r").readlines())]
#print(lines)

def splitter(line):
    splitted = line.split("|")
    return splitted

def extract_integers(input_string):
    # Define the regular expression pattern to match integers
    integer_pattern = r'\b\d+\b'

    # Use re.findall to find all matches in the input string
    integers = re.findall(integer_pattern, input_string)

    # Convert the matched strings to actual integers
    integers = [int(num) for num in integers]

    return integers

def finder(extracted_left, extracted_right):
    count = 0
    for left in extracted_left:
        if left in extracted_right:
            # print(f"found '{left}' in {extracted_right}")
            count += 1
            
    return count     

final = 0

deck = {}

for game_number, line in enumerate(lines, start=1):
    s = splitter(line)
    extracted_left = extract_integers(s[0])
    extracted_right = extract_integers(s[1])
    # final += finder(extracted_left, extracted_right)
    deck[game_number] = [(extracted_left[1:], extracted_right)]
print(deck)

game_to_play = 1
while game_to_play < len(lines):
    points = [finder(i,j) for i,j in deck[game_to_play]]
    # win_count = len(points)
    #print("game:", deck[game_to_play])
    #print("points,",points)
    for i in points:
        for j in range(1,i+1):
            deck[game_to_play+j].append(deck[game_to_play+j][0])
            # print("appended game", game_to_play+1, "-- ", deck[game_to_play+j][0])
    game_to_play +=1

score = 0 
for i, j in deck.items():
    print("this game",i,len(j)) 
    score += len(j)

print(score)