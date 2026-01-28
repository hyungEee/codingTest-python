exp=input().split('-') # -가 나올 때마다 문자열이 나뉘게 됨

ans=0

# 첫 덩어리는 더한다
ans+=sum(map(int,exp[0].split('+')))

# 나머지 덩어리는 모두 앞에 -가 붙은 것이므로,
# 이 덩어리들을 모두 괄호로 묶었다고 생각하고 모두 빼주면 됨
for part in exp[1:]:
    ans-=sum(map(int,part.split('+')))

print(ans)