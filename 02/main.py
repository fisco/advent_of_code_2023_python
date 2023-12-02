total = 0
game_power_total = 0

with open('input.txt', 'r') as f:
    for line in f:
        cube_maxes = { "red": 0, "green": 0, "blue": 0 }
        game_power = 1
        for game in line.split(": ")[1].strip().split("; "):
            for showing in game.split(", "):
                if int(showing.strip().split(" ")[0]) > cube_maxes[showing.strip().split(" ")[1]]:
                    cube_maxes[showing.strip().split(" ")[1]] = int(showing.strip().split(" ")[0])
        if cube_maxes["red"] <= 12 and cube_maxes["green"] <= 13 and cube_maxes["blue"] <= 14:
            total += int(line.split(": ")[0].strip().split(" ")[1])
        for key in cube_maxes:
            game_power *= cube_maxes[key]
        game_power_total += game_power
                     
print("The total is: " + str(total))
print("The game power total is: " + str(game_power_total))
