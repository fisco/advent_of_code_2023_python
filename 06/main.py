class Race:
    def __init__(self, time, distance_record):
        self.time = time
        self.distance_record = distance_record

    def number_of_ways_to_win(self):
        for i in range(0, int(self.time/2)):
            if i*(self.time-i) > self.distance_record:
                return 1 + self.time - (i*2);
        return 0


races = [
    Race(40, 219), 
    Race(81, 1012), 
    Race(77, 1365), 
    Race(72, 1089)
]

product = 1
for r in races:
    product *= r.number_of_ways_to_win()

print("Multiplying the total number of ways you could win these races yields: " + str(product))

big_race = Race(40817772, 219101213651089)
print("The number of ways you beat the record in this one much longer race is " + str(big_race.number_of_ways_to_win()))
