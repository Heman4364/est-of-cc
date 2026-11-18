
def subsets(nums):
    result = []

    def backtrack(i, path):
        if i == len(nums):
            result.append(path[:])
            return

        backtrack(i+1, path)

        path.append(nums[i])
        backtrack(i+1, path)
        path.pop()

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
