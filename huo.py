x11=int(input())
l=list(map(int,input().split()))

min1=min(l)
for p in range(len(l)):
    if min1!=l[p]:
        min2=l[p]
        break
for p in range(1,len(l)):
    if l[p]<min2 and l[p]>=min1:
        min2=l[p]
print(min2)
