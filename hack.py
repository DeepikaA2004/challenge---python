from itertools import combinations_with_replacement
s,n=input().split(' ')
s=sorted(s)

a=list(combinations_with_replacement(s,int(n)))
arr=[]
for i in a:
    s=''
    for j in i:
        s+=j
    arr.append(s)  
for i in arr:
   print(i)