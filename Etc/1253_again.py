def isgood(i,arr):
    target=arr[i]
    p1,p2=0,len(arr)-1
    
    while p1<p2:
        if p1==i:
            p1+=1
            continue
        if p2==i:
            p2-=1
            continue
        
        if arr[p1]+arr[p2]==target:
            return True
        elif arr[p1]+arr[p2]<target:
            p1+=1
        elif arr[p1]+arr[p2]>target:
            p2-=1

    return False        

n=int(input())
a=list(map(int,input().split()))
a.sort()

ans=0
for i in range(n):
    if isgood(i,a):
        ans+=1

print(ans)
            