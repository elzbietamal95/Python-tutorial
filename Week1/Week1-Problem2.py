s = 'azcbobobegghakl'
sum_bob = 0

for mark in range(len(s)):
    if s[mark] == 'b':
        if s[mark + 1] == 'o':
            if s[mark + 2] == 'b':
                sum_bob += 1

print(sum_bob)