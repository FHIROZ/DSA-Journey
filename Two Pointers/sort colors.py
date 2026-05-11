def sortcolors(arr):
    count0=count1=count2=0
    for i in range(len(arr)):
        if arr[i]==0:
           count0+=1
        if arr[i]==1:
           count1+=1
        if arr[i]==2:
           count2+=1
    for i in range(count0):
       arr[i]=0
    for i in range(count0,count0+count1):
       arr[i]=1
    for i in range(count0+count1,len(arr)):
       arr[i]=2
    return arr
arr=[0,2,2,1,0,1,0]
print(sortcolors(arr))