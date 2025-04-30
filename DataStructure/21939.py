import sys
import heapq

n=int(sys.stdin.readline())
problem1=[] # 최소 힙
problem2=[] # 최대 힙
exist=dict() # 문제 번호별로 현재 존재 여부 저장

for _ in range(n):
    p,l=map(int,sys.stdin.readline().split())
    # 힙에 문제 추가 및 존재 여부 업데이트
    heapq.heappush(problem1,(l,p)) 
    heapq.heappush(problem2,(-l,-p))
    exist[p]=l

m=int(sys.stdin.readline())
for _ in range(m):
    cmd=list(sys.stdin.readline().split())
    
    if cmd[0]=='add': # 문제 추가
        p,l=int(cmd[1]),int(cmd[2])
        heapq.heappush(problem1,(l,p))
        heapq.heappush(problem2,(-l,-p))
        exist[p]=l
        
    if cmd[0]=='solved': # 문제 풀이
        exist[int(cmd[1])]=-1 # 푼 문제는 존재 여부를 -1로 설정
        
    if cmd[0]=='recommend': # 문제 추천
        if int(cmd[1])==1: # 난이도 높은 문제
             while True:
                l,p=-problem2[0][0],-problem2[0][1]
                if exist[p] == l: # 저장된 난이도가 일치하는 경우 print
                    print(p)
                    break
                else: # 일치하지 않는 경우(이미 풀어서 -1이 되었거나, 풀었는데 다른 난이도로 다시 들어온 경우)
                    heapq.heappop(problem2)          
        elif int(cmd[1])==-1: # 난이도 작은 문제
            while True:
                l,p=problem1[0][0],problem1[0][1]
                if exist[p] == l:
                    print(p)
                    break
                else:
                    heapq.heappop(problem1)