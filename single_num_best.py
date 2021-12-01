def find_single(nums):
    a = 0 # XOR of any bit with 0 gives the bit

    for n in nums:
        a ^= n

    return a