# Two Sum

nums = [2,7,11,15]
target = 9

# Brute Force
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Optimal Solution
def twoSum(nums, target):
    sum_map = {}
    
    for i, num in enumerate(nums):
        diff = target - num

        if diff in sum_map:
            return [sum_map[diff], i]

        sum_map[num] = i 

print(twoSum(nums, target))
