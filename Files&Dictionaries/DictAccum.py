with open("travel_plans.txt", "r") as ref:
    characters = ref.read()
    letter_count = {}
    lines = 0
    for character in characters:
        if character != '\n':
            letter_count[character.lower()] = letter_count.get((character.lower()),0) + 1
        elif character == '\n':
            lines += 1

vowels = 0
occurrence = 0
lst = list(letter_count.keys())
for c in lst:
    if c in ['a','e','i','o','u']:
        vowels += 1
        occurrence += letter_count[c]

print("Number of lines:", lines)
print("Number of vowels:", vowels)
print("Occurrence of vowels only:", occurrence)
print("Occurrence of Words:" + "\n", letter_count)