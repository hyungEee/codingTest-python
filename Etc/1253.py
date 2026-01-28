n=int(input())
nums=list(map(int,input().split()))

nums.sort() # 시작하기에 앞서 입력받은 숫자들을 정렬
total=0

for i in range(n):
    start=0
    end=n-1
    
    while start<end:
        # 자기 자신의 경우 건너뛰어야 함
        if start==i:
            start+=1
            continue
        if end==i:
            end-=1
            continue
        
        sum=nums[start]+nums[end]
        
        if sum==nums[i]: # 두 수의 합이 목표값과 같은 경우 total++, break
            total+=1
            break
        elif sum<nums[i]: # 두 수의 합이 작을 경우 start 포인터 한 칸 뒤로
            start+=1
        elif sum>nums[i]: # 두 수의 합이 큰 경우 end 포인터 한 칸 앞으로
            end-=1      
        
print(total)