def FindPivot(nums):
    prefix=[0]*len(nums)
    prefix[0]=nums[0]
    for i in range(1,len(nums)):
        prefix[i]=prefix[i-1]+nums[i]
    sum1=prefix[-1]
    for i in range(len(prefix)):
        if i==0:
            leftsum=0
        else:
            leftsum=prefix[i-1]
        rightsum=sum1-prefix[i]
        if rightsum==leftsum:
            return i
    else:
        return -1
nums=[1,7,3,6,5,6]
print(FindPivot(nums))
# Output: 3