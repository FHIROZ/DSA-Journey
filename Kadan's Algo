def maxProduct(nums):

    prefix = 1
    suffix = 1

    answer = nums[0]

    n = len(nums)

    for i in range(n):

        if prefix == 0:
            prefix = 1

        if suffix == 0:
            suffix = 1

        prefix *= nums[i]

        suffix *= nums[n - 1 - i]

        answer = max(answer, prefix, suffix)

    return answer


nums = list(map(int, input("Enter array: ").split()))

print("Maximum Product Subarray:",
      maxProduct(nums))