import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
nge=[-1]*n
st=[]

for i in range(n-1,-1,-1): # 오른쪽에서부터 오큰수를 찾는다.
    while st:
        if st[-1]>nums[i]: # top이 현재 숫자보다 클 경우 오큰수는 top이 됨.
            nge[i]=st[-1]
            break
        else:
            st.pop() # top이 현재 숫자보다 작을 경우 pop하고 반복.
    st.append(nums[i]) # 현재 숫자를 스택에 추가해준다.

print(*nge)