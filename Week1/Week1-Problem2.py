s = 'azcbobobegghakl'
sum_bob = 0

for i in range(len(s)):
    if s[i] == 'b' and i != len(s) and i != len(s)-1 and i != len(s)-2:
        if s[i + 1] == 'o':
            if s[i + 2] == 'b':
                sum_bob += 1

print(sum_bob)