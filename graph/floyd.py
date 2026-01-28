INF=int(1e9)

def floyd(graph): # graph=간선에 대한 정보
    n=len(graph)
    dist = [row[:] for row in graph]  # 초기 거리 행렬 복사
    
    for k in range(n): # k = 경유 노드
        for i in range(n): # i = 시작 노드
            for j in range(n): # j = 도착 노드 
                if dist[i][k]!=INF and dist[k][j]!=INF: # i->k, k->j로 가는 길이 있는지 확인
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    # 현재 저장된 경로와 k를 거치는 경로 중 더 작은 것을 저장.