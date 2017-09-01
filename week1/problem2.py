s = "azcbobobegghakl"
counter = 0
for n in range(len(s)-1):
    if n + 2 > len(s) - 1:
        break
    elif s[n] == 'b' and s[n+1] == 'o' and s[n+2] == 'b':
        counter += 1
print("Number of times bob occurs is", counter)
