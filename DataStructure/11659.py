import sys
n,m=map(int, input().split())
nums=list(map(int, input().split()))
sum_nums=[0]
for i in range(n):
    sum_nums.append(sum_nums[-1]+nums[i])
for _ in range(m):
    i,j=map(int, sys.stdin.readline().split())
    print(sum_nums[j]-sum_nums[i-1])