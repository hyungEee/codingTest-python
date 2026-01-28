import sys

input=sys.stdin.readline
n=int(input())
cus=[]
for _ in range(n):
    cus.append(int(input()))

# 팁이 음수가 되면 어차피 모두 0으로 처리되기 때문에
# 팁을 많이 주는 사람부터 응대하는 것이 제일 이득이다.
# 팁을 많이 주는 순서대로 정렬한다.
cus.sort(reverse=True)

# 팁 계산
ans=0
for i in range(n):
    tip=cus[i]-i
    if tip>0:
        ans+=tip
        
print(ans)