import sys
import heapq 

n=int(sys.stdin.readline())
table=[]

for _ in range(n):
    l=list(map(int,sys.stdin.readline().split()))
    for item in l:
        heapq.heappush(table,item) # 숫자들을 힙 형태로 저장
    while len(table)>n:
        heapq.heappop(table)  # n번째 큰수보다 작은수들은 반복때마다 메모리를 위해 모두 버린다

print(heapq.heappop(table)) # 이제 힙에서 가장 작은 수 == n번째 큰수가 되었다