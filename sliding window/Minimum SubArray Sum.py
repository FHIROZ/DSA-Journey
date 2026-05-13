def MinSubarray(arr,target):
    left,sum_value=0,0
    minlen=float('inf')
    n=len(arr)
    for right in range(n):
        sum_value+=arr[right]
        while(sum_value>=target):
            minlen=min(minlen,right-left+1)
            sum_value-=arr[left]
            left+=1
    return minlen
    if minlen==float('inf'):
        return 0

arr=[2,3,1,2,4,3]
target=7
print(MinSubarray(arr,target))
