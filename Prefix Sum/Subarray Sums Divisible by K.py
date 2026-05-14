from collections import defaultdict
def subarraysDivByK (nums, k):        
    freq=defaultdict(int)
    prefix,ans=0,0
    freq[0]=1
    for num in nums:
        prefix+=num
        rem=prefix%k
        ans+=freq[rem]
        freq[rem]+=1
    return ans
nums=[4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums,k))
