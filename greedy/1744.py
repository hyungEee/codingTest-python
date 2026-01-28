import sys
input=sys.stdin.readline

n=int(input())

# 같은 부호면서 절댓값이 가장 큰 수부터 묶어야 가장 큰 수가 된다
# 음수가 한개 남을 경우 0을 곱해 없애줄 수 있다.
# 따라서 양수 음수 0입력여부를 나누어 저장해준다.
pos=[]
neg=[]
zero=False
for _ in range(n):
    num=int(input())
    if num>0:
        pos.append(num)
    elif num<0:
        neg.append(num)
    else:
        zero=True
        
ans=0

# 양수 (정렬한 뒤 큰 수부터 곱해서 차례로 더해줌)
pos.sort()
while len(pos)>1:
    n1=pos.pop()
    n2=pos.pop()
    if n1==1 or n2==1: # 두 숫자 중 하나가 1일 경우엔 그냥 더하는게 더 큼
        ans+=n1+n2
    else:
        ans+=n1*n2
if pos:
    ans+=pos.pop() # 수가 남아있다면 더해줌

# 음수 (정렬한 뒤 작은수(절대값이 큰 수)부터 곱해서 더해줌)
neg.sort(reverse=True)
while len(neg)>1:
    ans+=neg.pop()*neg.pop()
if neg:
    if not zero: # 0이 없다면 남아있는 음수를 그냥 더해줌
        ans+=neg.pop()
    # 0이 있을 경우 남아있는 음수와 곱해져 상쇄된다.
    
print(ans)
