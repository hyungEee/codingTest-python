from collections import deque

n=int(input())
m=int(input())
material=list(map(int,input().split()))
material.sort()
material=deque(material)

ans=0
num=material[0]+material[-1]
while True:
    if num==m:
        ans+=1
        material.pop()
        material.popleft()
    elif num<m:
        material.popleft()
    elif num>m:
        material.pop()
    
    if len(material)<2:
        break
    num=material[0]+material[-1]

print(ans)