'''
s = "abciiidef"
k = 3
r = h = 0
vowel = set('aeiou')
for i, c in enumerate(s):
    if c in vowel: h += 1
    if i >= k and s[i - k] in vowel: h -= 1
    r = max(r, h)
print(r)

'''
def binpo(a,n):
    res = 1
    while(n>0):
        if (b&1)



print(binpo(3,13))

