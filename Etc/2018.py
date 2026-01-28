n=int(input())

total=1 # 자기 자신만 있는 경우를 더하고 시작했
start=1
end=2
sum=start+end

while start<end:
    if sum<n: # sum이 n보다 작으면 큰 수를 더해줌. (end 포인터++, sum에 늘린 수를 더해주기)
        end+=1
        sum+=end
    elif sum>n: # sum이 n보다 크면 작은 수를 빼줌. (sum에서 start 빼주기, start 포인터++)
        sum-=start
        start+=1
    elif sum==n: # sum==n이면 total++, start한칸 옮기고 다시 탐색
        total+=1
        sum-=start
        start+=1
        
print(total)
