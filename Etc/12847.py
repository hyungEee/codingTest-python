# n개의 일급 리스트 t에서 연속 m일 일급 합의 최대값을 구하는 문제
n,m=map(int,input().split())
t=list(map(int,input().split()))

# 윈도우 초기값 셋팅
max=0
total=0
for i in range(m):
    total+=t[i]
max=total

for i in range(m,n): # 윈도우를 한칸씩 옮겨가며 최대값 구하기
    total-=t[i-m] # 이전 값 빼주기
    total+=t[i] # 새로운 값 더해주기
    if total>max:
        max=total # 기존 max 값보다 클 경우 교체
        
print(max)