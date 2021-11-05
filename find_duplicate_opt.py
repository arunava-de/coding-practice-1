def find_dup(nums):
    n = len(nums)

    if n==2:
        return nums[0]

    slow = nums[0]
    fast = nums[0]

    while slow!=fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = nums[0]
    while slow!=fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast 