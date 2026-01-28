from collections import deque

n,m=map(int,input().split())
lab=[list(map(int,input().split())) for _ in range(n)]

# 빈칸, 바이러스 좌표들을 모두 모아서 저장
empty=[]
virus=[]
for i in range(n):
    for j in range(m):
        if lab[i][j]==0:
            empty.append((i,j))
        elif lab[i][j]==2:
            virus.append((i,j))

# backtracking 방식으로 벽 설치 조합을 모두 구했다.
# Leetcode Combinations 문제와 같은 방식
combis=[]
def getCombis(start,coms):
    if len(coms)==3:
        combis.append(coms)
        return
    for i in range(start, len(empty)):
        getCombis(i+1,coms+[empty[i]])
getCombis(0,[])

# 바이러스 확산 bfs
dr=[0,0,1,-1]
dc=[1,-1,0,0]
def spread(arr):
    dq=deque(virus)
    while dq:
        r,c=dq.popleft()
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<m and arr[nr][nc]==0:
                arr[nr][nc]=2
                dq.append((nr,nc))
    safe=sum(row.count(0) for row in arr)
    return safe
        
# 각 조합마다 벽세우기 -> 바이러스 확산 및 최댓값 갱신
maxSafe=0
for com in combis:
    newLab = [row[:] for row in lab]
    
    for r,c in com: # 벽 세우기
        newLab[r][c]=1
    
    maxSafe=max(maxSafe,spread(newLab)) # 바이러스 확산 및 최댓값 갱신

print(maxSafe)