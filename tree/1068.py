
n=int(input()) # 노드 개수
parent=list(map(int,input().split())) # 부모노드 정보
m=int(input()) # 지울 노드

tree=[[] for _ in range(n)] # 자식노드 정보 저장
root=0 # 0번 노드가 루트가 아닐 수 있으므로 찾아서 따로 저장해놔야함!! 

for i in range(n):
    if parent[i]==-1:
        root=i
        continue
    tree[parent[i]].append(i)
    
# dfs
def dfs(x):

    if x==m: # m이 나오면 그 하위 노드는 건너뜀
        return 0
    
    if not tree[x]: # 리프노드인 경우
        return 1
    
    leaf=0
    hasOnlyM=True # m만 자식으로 갖고있는지 여부
    for node in tree[x]:
        if node!=m: # m제외하고 dfs, 다른 자식이 있는 경우이므로 hasOnlyM을 False로 바꿔줌
            hasOnlyM=False 
            leaf+=dfs(node)
    
    if hasOnlyM: # m만 자식으로 갖고있을 경우
        return 1
    
    return leaf

print(dfs(root))
    