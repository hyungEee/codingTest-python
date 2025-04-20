import sys

n,k=map(int,sys.stdin.readline().split())
num=[int(i) for i in list(sys.stdin.readline().rstrip())]
st=[]
count=0

for i in num:
    while st and count<k and st[-1]<i: 
            # top이 현재 추가하려는 숫자보다 작을때만 실행한다 큰수가 나오면 빠져나온다
            st.pop()
            count+=1
    st.append(i) # 현재 숫자를 추가한다

if count<k: # 카운트를 다 채우지 못한경우(내림차순으로 정렬된 경우)
    while count<k: # 카운트 다 채울때까지 뒤에서부터 삭제해준다
        st.pop()
        count+=1
print(*st,sep="")