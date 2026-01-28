import heapq  # 우선순위 큐를 사용하기 위한 모듈
def dijkstra(graph, start): # graph=간선에 대한 정보, start=시작노드
    dist = [float('inf')] * len(graph)  # 최단경로 테이블, 모든 거리 무한대로 초기화
    dist[start] = 0  # 시작 노드의 최단경로는 0으로 설정해준다.
    pq = [(0, start)]  # (거리, 노드) 형태로 우선순위 큐에 삽입

    while pq:
        current_dist, u = heapq.heappop(pq)  # 최단 거리 노드 꺼내기

        # pq에서 꺼낸 거리가 이미 갱신된 거리인 dist[u]보다 크다면 무시
        if current_dist > dist[u]:
            continue

        # 현재 노드의 인접 노드 탐색
        for v, weight in graph[u]:
            new_dist = current_dist + weight  # 새로운 거리 계산

            if new_dist < dist[v]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                dist[v] = new_dist  # 더 짧은 거리로 갱신
                heapq.heappush(pq, (new_dist, v))  # 갱신된 노드 추가
    
    return dist