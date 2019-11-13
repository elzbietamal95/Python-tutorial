s = 'azcbobobegghakl'
total_vowels = 0

for letter in s:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        total_vowels += 1

print(total_vowels)