from collections import deque

n,m=map(int, input().split())

arr=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    visited=[-1]*(n+1)

    q=deque()
    q.append(start)
    visited[start]=0

    while q:
        cur=q.popleft()
        for next in arr[cur]:
            if visited[next]==-1:
                visited[next]=visited[cur] + 1
                q.append(next)
    total=sum(visited)
    return total

min=int(1e9)
ans=0
for i in range(1,n+1):
    total=bfs(i)
    if total<min:
        min=total
        ans=i

print(ans)