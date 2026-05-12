def subarrays(arr,k):
    n=len(arr)
    res=[]
    count=0
    for i in range(n):
        product=1
        for j in range(i,n):
            product *= arr[j]
            if product < k:
                count += 1
            else:
                break
    return count




nums = [10,5,2,6]
k = 100
print(subarrays(nums,k))