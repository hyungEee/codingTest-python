import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())
circle=deque([i for i in range(1,n+1)])
ans=[]

for i in range(n):
    for j in range(k-1):
        circle.append(circle.popleft())
    ans.append(circle.popleft())
print("<",end="")
print(*ans,sep=", ",end=">")