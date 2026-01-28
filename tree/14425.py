import sys

n,m=map(int,input().split())
s=[]
for _ in range(n):
    s.append(sys.stdin.readline())

total=0
for _ in range(m):
    test=sys.stdin.readline()
    if test in s:
        total+=1
        
print(total)