import sys
from collections import deque

n=int(sys.stdin.readline())
dq=deque([])

for _ in range(n):
    cmd=list(sys.stdin.readline().split())
    if cmd[0]=='push_front':
        dq.appendleft(cmd[1])
    elif cmd[0]=='push_back':
        dq.append(cmd[1])
    elif cmd[0]=='pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0]=='pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(dq))
    elif cmd[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd[0]=='back':
        if dq:
            print(dq[-1])
        else:
            print(-1)