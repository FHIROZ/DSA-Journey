def movezeros(arr):
    j=0
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(j)

    return arr

arr=[0,20,2,0,7,0,1,2,0]
print(movezeros(arr))