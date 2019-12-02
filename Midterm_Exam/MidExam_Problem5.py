def print_without_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    removed = s
    for letter in s:
        if letter in vowels:
            removed = removed.replace(letter, '')

    print(removed)

s = "This is great!"
print_without_vowels(s)