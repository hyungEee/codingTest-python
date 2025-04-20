import sys
from collections import deque # List 사용할 경우 pop(0)연산이 매우 느리기 때문에 시간이 오래걸림.
# 시간을 줄이기 위해 deque를 사용한다!!!

t=int(sys.stdin.readline())
for _ in range(t):
    reversed=False
    errored=False
    cmd=list(sys.stdin.readline().rstrip())
    n=int(sys.stdin.readline())
    if n!=0:
        arr=deque(map(int,sys.stdin.readline().strip('[]\n').split(','))) # []와 ,를 제거하고 리스트로 만들기
    else:
        sys.stdin.readline() 
        arr=deque() # n==0이면 빈 배열을 만들어줌

    for c in cmd:
        if c=='R':
            reversed=not reversed # R 명령어가 들어오면 방향을 바꿔줌
        if c=="D":
            if not arr: # 빈 배열에 D 명령어가 적용될 경우 error 처리
                errored=True
                print("error")
                break
            if reversed: # 방향 바뀐 상태면 맨 뒤 값을 pop
               arr.pop()
            else:
                arr.popleft() # 방향 안바뀐 상태면 맨 처음 값을 pop
    if not errored: # 에러가 발생 안한 경우에만 실행 (주의: 빈 배열이지만 에러가 안난 경우도 있음!)
        if reversed:
            arr.reverse() # 뒤집어진 경우 배열 뒤집어준다..
        print("[",end="")
        print(*arr,sep=",",end="]\n")