def four_sum_count(nums1, nums2, nums3, nums4):
    sum_map = dict()
    count = 0

    for i in len(nums1):
        for j in len(nums2):
            sum_map[nums1[i]+nums2[j]] = sum_map.get(nums1[i]+nums2[j], 0) + 1

    for i in len(nums3):
        for j in len(nums4):
            if -(nums3[i]+nums4[j]) in sum_map:
                count += sum_map[nums3[i]+nums4[j]]

    return count 