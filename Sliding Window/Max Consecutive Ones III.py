def longestOnes(nums, k):
        left=0
        right=0
        maxlen=0
        length=0
        n=len(nums)
        zeros=0
        while(right<n):
           
            if nums[right]==0:
                zeros+=1
            if zeros<=k:
                length=right-left+1
                maxlen=max(maxlen,length)
            right+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
        return maxlen
arr=[1,1,1,0,0,0,1,1,1,1,0]
k=2
print(longestOnes(arr,k))
