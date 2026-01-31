from collections import deque

n,l=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
dq=deque([])

for i in range(n):
    now=a[i]
    
    while dq and dq[-1][1]>now: # 덱의 마지막 위치에서부터 now보다 큰 값은 제거
        dq.pop()
    dq.append((i,now)) # 마지막 위치에 now값 저장
    while dq and dq[0][0]<=i-l: # 덱의 처음 위치에서부터 L 범위를 벗어난 값은 제거
        dq.popleft()
    
    if not dq:
        dq.append((i,now))
    ans.append(dq[0][1]) #덱의 첫번째 데이터 저장

print(*ans)