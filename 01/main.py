import re

text_to_day = {
      "one": "o1e", 
      "two": "t2o",
      "three": "th3ee",
      "four": "fo4ur", 
      "five": "fi5ve", 
      "six": "s6x",
      "seven": "se7en", 
      "eight": "ei8ht", 
      "nine": "ni9ne"}

calibration = 0

with open('input.txt', 'r') as f:
    for line in f:
        for key in text_to_day:
            pattern = re.compile(key)
            line = re.sub(pattern, text_to_day[key], line)
        line = re.sub(r"[^\d]", "", line)
        if len(line) == 1:
            line = line + line
        if len(line) > 2:
            line = line[0] + line[-1]
        calibration += int(line)

print(calibration)
