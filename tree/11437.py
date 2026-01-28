import sys
sys.setrecursionlimit(100000) # 재귀함수 사용시 필수..

n=int(input())
graph=[[] for _ in range(n+1)] # 노드 정보
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent=[0]*(n+1) # 각 노드의 부모노드 정보
depth=[0]*(n+1) # 각 노드까지의 깊이
visited=[False]*(n+1) # 방문 여부

# dfs로 트리를 방문하며 부모노드 정보와 깊이정보를 초기화해줌
def dfs(x,d):
    visited[x]=True
    depth[x]=d 
    for node in graph[x]:
        if not visited[node]:
            parent[node]=x
            dfs(node,d+1)
            
dfs(1,0)

def lca(a,b):
    # 먼저 두 노드의 깊이를 맞춰줌(깊이 얕은쪽으로 맞춤)
    while depth[a]!=depth[b]:
        if depth[a]>depth[b]:
            a=parent[a]
        else:
            b=parent[b]
    
    # 두 노드가 같아질때까지 부모노드로 이동을 반복
    while a!=b:
        a=parent[a]
        b=parent[b]
    
    return a

m=int(input())
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    print(lca(a,b))
