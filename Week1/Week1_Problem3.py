s = 'azcbobobegghakl'

substring = s[0]
check = s[0]
for char in s[1:]:
    if (check[-1] <= char):
        check += char
        if (len(substring) < len(check)):
            substring = check
    else:
        check = char


print("Longest substring in alphabetical order is:", substring)