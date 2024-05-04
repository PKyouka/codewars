def pipe_fix(nums):
    for i in nums:
        if i == nums[0]:
            start = i
        elif i == nums[-1]:
            end = i
    return list(range(start, end+1))