import sys
import heapq

n=int(sys.stdin.readline())
pos=[] # 양수값을 저장하는 배열
neg=[] # 음수값을 저장하는 배열

for i in range(n):
    x=int(sys.stdin.readline())
    if(x!=0):
        if(x>0):
            heapq.heappush(pos,x) # 힙에 절대값 추가
        else:
            heapq.heappush(neg,-x) # 힙에 절대값 추가
    else:
        if not pos and not neg: # 힙이 비었을 겨웅 0 출력
            print(0)
        elif pos and not neg: # 양수만 있을 때
            print(heapq.heappop(pos))
        elif neg and not pos: # 음수만 있을 때
            print(-heapq.heappop(neg))
        else:
            p=pos[0]
            n=neg[0]
            # 절대값을 비교하여 더 작은 수 출력
            # 절대값이 같은 경우에는 음수를 출력
            if p<n: 
                print(heapq.heappop(pos))
            elif n<=p:
                print(-heapq.heappop(neg))