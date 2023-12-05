card_values = []
card_number_of_matching_numbers = []
cards_you_have = []

with open('input.txt', 'r') as f:
    for line in f:
        game_part = line.split(" | ")[0]
        winners_part = line.split(" | ")[1]
        card_value = 0
        nm = 0
        for w in winners_part.strip().split():
            card_numbers_part = game_part.split(": ")[1]
            for n in card_numbers_part.strip().split():
                if int(n) == int(w):
                    nm += 1
                    if card_value == 0:
                        card_value = 1
                    else:
                        card_value *= 2
        card_values.append(int(card_value))
        card_number_of_matching_numbers.append(nm)

for i in card_number_of_matching_numbers:
    cards_you_have.append(1)

for i in range(len(card_number_of_matching_numbers)):
    if card_number_of_matching_numbers[i] > 0:
        for j in range(min(i+1, len(card_number_of_matching_numbers)-1), min(i+1+card_number_of_matching_numbers[i], len(card_number_of_matching_numbers))):
            cards_you_have[j] += cards_you_have[i]

print("The simple value of all the cards is: " + str(sum(card_values)))
print("The number of cards you have is: " + str(sum(cards_you_have)))
