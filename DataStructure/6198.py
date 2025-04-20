import sys

n=int(sys.stdin.readline())
heights=[] # 빌딩들의 높이
total=[0]*n # 각 빌딩마다 확인할 수 있는 빌딩의 수

for _ in range(n):
    heights.append(int(sys.stdin.readline()))

st=[] # 빌딩의 인덱스를 저장
for i in range(n-1,-1,-1):
    while st and heights[i]>heights[st[-1]]:
        total[i]+=total[st.pop()]+1
    st.append(i)
print(sum(total))

# 자신의 오른쪽에 있는 빌딩 중에,
# 자신보다 크거나 같은 값이 나오기 전까지 볼 수 있음
# 오른쪽 원소부터 스택에 추가하고,
# 현재 값이 top보다 크면 스택 pop, 현재값의total=pop한 값의total+1
# 다끝나면 현재값을 스택에 추가