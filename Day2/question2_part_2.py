dataset = open("input2.txt", "r")
games = []
class Game:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

def take_the_biggest_color_and_convert(game_plays):
    red = 0
    green = 0 
    blue = 0 
    for i in game_plays:
        if i[1] == "red" and i[0] > red:
            red = i[0]
        if i[1] == "green" and i[0] > green:
            green = i[0]
        if i[1] == "blue" and i[0] > blue:
            blue = i[0]

    return (red,green,blue)
    

def calculate_power(colors):
    answer = 1
    for i in colors:
        answer *= i
    return answer

def spliter(line):
    splitted = line.split(":")
    splitted_id = splitted[0].split(" ")[1]
    print(splitted_id)
    rest = splitted[1]
    games = rest.strip().split(";")
    game_elements = []
    for game in games:
        t = game.strip().split(",")
        for i in t:
            semi = i.strip().split(" ")
            semi[0] = int(semi[0])
            game_elements.append(semi)
    return splitted_id, game_elements

# only 12 red cubes, 13 green cubes, and 14 blue cubes
game_zero = (0, (12,13,14))
def check_if_possible(game):
    game_id = game[0]
    game_content = game[1]
    if (game_content[0] > 12 or game_content[1] > 13 or game_content[2] > 14):
        return False, 0
    return True, int(game_id)

power_ans = 0
for line in dataset.readlines():
    s = spliter(line)
    s =(s[0] , take_the_biggest_color_and_convert(s[1]))
    print(s[1])
    power_ans += calculate_power(s[1])
    
print(power_ans)

#(13, (3,4,5), (4,5,6))