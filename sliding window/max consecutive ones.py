def maxConsecutiveOnes(arr):
    maxi=0
    count=0
    for i in arr:
        if i==1:
            count+=1
            if(count>maxi):
                maxi=count 
        else:
            count=0
    return maxi
arr=[0,1,1,0,1,1,1,0]
print(maxConsecutiveOnes(arr))
