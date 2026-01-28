n,m=map(int,input().split())

nums={i:[i] for i in range(n+1)}

for _ in range(m):
    c,a,b=map(int,input().split())
    
    if c==0:
        
