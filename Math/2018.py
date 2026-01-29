n=int(input())

total=1 # 자기자신의 1가지 경우

p1,p2=1,2
num=p1+p2
while p1<p2:
    if num==n:
        total+=1
        p2+=1
        num+=p2
    elif num<n:
        p2+=1
        num+=p2
    elif num>n:
        num-=p1
        p1+=1

print(total)