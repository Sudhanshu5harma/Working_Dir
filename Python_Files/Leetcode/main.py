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



nums = [3,7]
nums.sort()
m1 = nums[len(nums)-1]
m2 = nums[len(nums)-2]
res = (m1-1)*(m2-1)
print(res)

'''
h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]

horizontalCuts.append(h)
verticalCuts.append(w)
horizontalCuts.append(0)
verticalCuts.append(0)
horizontalCuts.sort()
verticalCuts.sort()
hd = []
vd = []
for i in range(len(horizontalCuts)-1):
    dif1 = horizontalCuts[i+1]-horizontalCuts[i]
    hd.append(dif1)

for j in range(len(verticalCuts)-1):
    dif2 = verticalCuts[j+1]-verticalCuts[j]
    vd.append(dif2)
res =[]
for  t in vd:
    for y in hd:
        res.append(t*y)

print(max(res)) mo10^9


