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
'''''

'''
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
'''
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
