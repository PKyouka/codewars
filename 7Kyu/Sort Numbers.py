def solution(nums):
    if not nums:
        return []
    try:
        nums.sort()
        return nums
    except:
        return None