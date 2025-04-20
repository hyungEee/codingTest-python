from heapq import heapify,heappush,heappop
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville)>1:
        if scoville[0]>=K:
            break
        mixed=heappop(scoville)+heappop(scoville)*2
        heappush(scoville,mixed)
        answer+=1
    if scoville[0]>=K:
        return answer
    else:
        return -1