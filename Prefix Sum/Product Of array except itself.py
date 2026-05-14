def ProductArray(arr):
    n=len(arr)
    prefix=[1]*n
    suffix=[1]*n
    ans=[1]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]*arr[i]
    suffix[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        suffix[i]=suffix[i+1]*arr[i]

    for i in range(n):
        if i == 0:
            ans[i]=suffix[i+1]
        elif i==n-1:
            ans[i]=prefix[i-1]
        else:
            ans[i]=prefix[i-1]*suffix[i+1]
    return ans
arr=[1,2,3,4]
print(ProductArray(arr))