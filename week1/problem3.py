s = "rcnudjzqmedfyocnjbamgjvk"
result = ""
temp = s[0]
for n in range(len(s) - 1):
    if s[n] <= s[n+1]:
        temp += s[n+1]
    else:
        if len(temp) > len(result):
            result = temp
        temp = s[n+1]

if len(temp) > len(result):
    result = temp

print("Longest substring in alphabetical order is: ", result)
