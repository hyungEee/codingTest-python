import sys

n=int(sys.stdin.readline())
seq=[]
for _ in range(n):
    seq.append(int(sys.stdin.readline()))
nums=[i for i in range(n,0,-1)]
st=[]
op=[]

for i in range(n):
    while True:
        if st and st[-1]==seq[i]: # 맞추려는 수열의 숫자==스택 top이라면 pop  
            st.pop()
            op.append("-")
            break
        if st and st[-1]>seq[i]: # 수열의 숫자가 이미 push된 수인데도 스택 top보다 작다면 수열을 만들 수 없음.
            op=[]
            break
        st.append(nums.pop()) # 맞추려는 수열의 숫자가 될때까지 스택에 push한다.
        op.append("+")
    if not op:
        break
if op:
    for i in op:
        print(i)
else:
    print("NO")
