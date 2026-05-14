def checkSubarraySum(nums, k):
    mp = {0: -1}

    total = 0

    for i in range(len(nums)):

        total += nums[i]

        rem = total % k

        # remainder already seen
        if rem in mp:

            # subarray length >= 2
            if i - mp[rem] >= 2:
                return True

        else:
            # store first occurrence only
            mp[rem] = i

    return False
nums = [23,2,6,4,7]
k = 13
print(checkSubarraySum(nums,k))