def FruitsBasket(arr):
    freq={}
    left,maxlen=0,0
    for right in range(len(arr)):
        if arr[right] in freq:
            freq[arr[right]]+=1
        else:
            freq[arr[right]]=1
        while len(freq)>2:
            freq[arr[left]]-=1
            if freq[arr[left]]==0:
                del freq[arr[left]]
            left+=1
        maxlen=max(maxlen,right-left+1)
    return maxlen
arr=[3,3,3,1,2,1,1,2,3,3,4]
print(FruitsBasket(arr))
