import sys
import heapq
input=sys.stdin.readline

# 카드갯수가 작은 묶음부터 합쳐야 합칠때마다 비교 횟수가 가장 적게 된다
# 따라서 힙 자료구조를 사용했다.

n=int(input())
card=[]
for _ in range(n):
    heapq.heappush(card,int(input()))

ans=0
while len(card)>1:
    # 갯수가 가장 적은 카드 묶음 두개를 합친다.
    c1=heapq.heappop(card)
    c2=heapq.heappop(card)

    # 합친 카드묶음을 다시 힙에 추가한다.
    heapq.heappush(card,c1+c2)
    
    # 비교 횟수 더해주기
    ans+=(c1+c2)

print(ans)
