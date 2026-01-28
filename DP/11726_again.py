n=int(input())
dp=[0]*1001

dp[1]=1 # 세로타일 1개
dp[2]=2 # 세로타일2, 가로타일2

# dp[3]=dp[2]에 세로타일1 더하는 방법 + dp[1]에 가로타일2 더하는 방법
# 따라서 dp[n]=dp[n-1]+ dp[n-2]

for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
    
print(dp[n]%10007)