class TranslatableValue:
    source_range_start = None
    source_range_end = None
    destination_range_start = None

    def __init__(self, source_range_start, source_range_end, destination_range_start):
        self.source_range_start = source_range_start
        self.source_range_end = source_range_end
        self.destination_range_start = destination_range_start

class TranslatableCollection:
    def __init__(self, file_name):
        self.translatables = []

        with open(file_name, 'r') as f:
            for line in f:
                ns = line.split()
                # print(ns)
                destination_range_start = int(ns[0])
                source_range_start =  int(ns[1])
                range_length = int(ns[2])
                self.translatables.append(TranslatableValue(source_range_start, source_range_start + range_length - 1, destination_range_start))

    def translated_value(self, number):
        for t in self.translatables:
            if (number >= t.source_range_start) and (number <= t.source_range_end):
                return t.destination_range_start + (number - t.source_range_start)
        return number

seeds = []
seed_to_soil = TranslatableCollection("seed-to-soil.txt")
soil_to_fertilizer = TranslatableCollection("soil-to-fertilizer.txt")
fertilizer_to_water = TranslatableCollection("fertilizer-to-water.txt")
water_to_light = TranslatableCollection("water-to-light.txt")
light_to_temperature = TranslatableCollection("light-to-temperature.txt")
temperature_to_humidity = TranslatableCollection("temperature-to-humidity.txt")
humidity_to_location = TranslatableCollection("humidity-to-location.txt")

with open("seeds.txt", 'r') as f:
    for line in f:
        for s in line.split():
            seeds.append(int(s))

locations = []
for s in seeds:
    soil = seed_to_soil.translated_value(s)
    fertilizer = soil_to_fertilizer.translated_value(soil)
    water = fertilizer_to_water.translated_value(fertilizer)
    light = water_to_light.translated_value(water)
    temperature = light_to_temperature.translated_value(light)
    humidity = temperature_to_humidity.translated_value(temperature)
    location = humidity_to_location.translated_value(humidity)
    locations.append(location)

lowest_location = 0
for i in range(0, 20, 2):
    print("--- " + str(i))
    print("Processing: " + str(seeds[i]) + " - " + str(seeds[i]+seeds[i+1]))
    # print("Processing: " + str(seeds[i+1]))
    # print("Processing: " + str((seeds[i]+seeds[i+1]) - seeds[i]))
    for s in range(seeds[i], (seeds[i]+seeds[i+1]), 1):
        # print("seed: " + str(s))
        soil = seed_to_soil.translated_value(s)
        fertilizer = soil_to_fertilizer.translated_value(soil)
        water = fertilizer_to_water.translated_value(fertilizer)
        light = water_to_light.translated_value(water)
        temperature = light_to_temperature.translated_value(light)
        humidity = temperature_to_humidity.translated_value(temperature)
        location = humidity_to_location.translated_value(humidity)
        if (lowest_location == 0) or (location < lowest_location):
            lowest_location = location

print("The lowest location number that corresponds to any of the initial seed numbers is " + str(min(locations)))
print("The lowest location number that corresponds to any of the initial seed numbers using ranges is " + str(lowest_location))

