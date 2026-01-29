import sys

n,m=map(int,input().split())
nums=[]
for _ in range(n):
    nums.append(list(map(int,sys.stdin.readline().split())))

# 2차원 누적합 구하기
# 공식: s[i][j]=s[i][j-1]+s[i-1][j]-s[i-1][j-1]+a[i][j] (s:누적합배열, a:원본배열)
sums=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        sums[i][j]=sums[i][j-1]+sums[i-1][j]-sums[i-1][j-1]+nums[i-1][j-1]
    
for _ in range(m):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    total=sums[x2][y2]-sums[x1-1][y2]-sums[x2][y1-1]+sums[x1-1][y1-1]
    print(total)