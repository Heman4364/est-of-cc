
def subsets(nums):
    n = len(nums)
    result = []

    for i in range(2**n):
        temp = []

        for j in range(n):
            if i & (1 << j):
                temp.append(nums[j])

        result.append(temp)

    return result

print(subsets([1, 2, 3]))
