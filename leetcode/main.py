'''import heapq
import itertools
from itertools import product
mat = [[1,3,11],[2,4,6]]
k = 5
#nums1= [ 1,  5,  9]
#nums2 =[10, 11, 13]
#nums3 = [12, 13, 15]
#k =5 , key=sum)[:k])
val= [mat[i] for i in range(len(mat))]
val = [[j for j in range(len(mat))] for i in range(len(mat))]
j = list(map(list, heapq.nsmallest(k+1,sorted(itertools.product(*mat)))))
i = (sorted(list(product(*mat))))
print(sum(j[k-1]))

paths = [["B","C"],["D","B"],["C","A"]]
for i,n in enumerate(paths):
    #print(i)
    for j,p in enumerate(n):
        k = sum(p in item for item in paths)
        if k ==1 & j ==1:
            print(p)



J = "z"
S = "ZZ"
K =0
j = list(J)
s = list(S)
for i in S:
    k =  sum(i in item for item in J)
    K +=k
print(K)

ransomNote = "fffbfg"
magazine = "effjfggbffjdgbjjhhdegh"
ran = Counter(ransomNote)
mag = Counter(magazine)
for c in ran:
    print(c)
    print(mag[c])
    if c not in mag or mag[c]<ran[c]:

        print (False)
print(True)

def flip(c):
    return '1' if (c == '0') else '0'
n = 1
c = bin(n).replace('0b','')
c = list(c)
b = []
for i in c:
     b.append(flip(i))
d = "".join(b)
print(int(d,2))


s = ""
res =[]
if s=='':
    print(-1)
else
for n,i in enumerate(s):
    if s.count(i)==1:
        res.append(n)
        break
    else:
        res.append(-1)
print(max(res))


from collections import Counter
c = [2,2,1,1,1,2,2]

s = Counter(c).most_common()
return s[0][0]


arr1 = [10, 5, 2, 23, 19]
arr2 = [19, 5, 3]
res = []
for i in arr2:
    if (i in arr1):
        res.append(1)
if len(res)==len(arr2):
    print("Yes")
else:
    print("No")
'''


n = 5
k = 3
rq,cq = 4,3
chess = [[0 for i in range(n)] for j in range(n)]
#chess[rq-1][cq-1]=2
#hori
for i in range(n):
    chess[rq-1][i]=1
for j in range(n):
    chess[j][cq-1]=1
#dia
for k in range(n):
    chess[rq-1-k][cq-1-k]=1

for p in range(n):
    #while((rq-1+p)<=n and (cq-1+p)<=n ):
     chess[rq-1+p][cq-1+p]=1



chess[rq-1][cq-1]=2
for i in chess:
    print(i)