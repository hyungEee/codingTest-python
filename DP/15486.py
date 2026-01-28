import sys

n=int(input()) # 주어진 n일
tp=[[] for _ in range(n+1)] # 상담일정표
tp[0]=[0,0]
for i in range(1,n+1):
    tp[i]=list(map(int,sys.stdin.readline().split()))

dp=[0]*(n+2) # 일자별 최대 수익, n+2까지 만들어야 마지막 날 수익도 반영됨 주의!!

for i in range(1,n+1):     
    t,p=tp[i]
    
    # i일에 상담 하지 않는 경우
    # 현재 i일의 최대 수익과 전날의 수익을 유지할 경우 최대 수익 중 더 큰 값 
    dp[i]=max(dp[i],dp[i-1])
    
    # i일 상담 일정이 기간을 초과하는 경우 패스
    if i+t-1>n:
        continue

    # 상담을 하는 경우
    # 해당 상담 완료 후 수익 값을 반영해줌(새로 구한 값과 원래 값 중 더 큰 값)
    dp[i+t]=max(dp[i]+p,dp[i+t])

print(max(dp))