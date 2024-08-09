def use_insertion_sort(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            break
        if nums[i] > nums[i + 1]:
            # Swap the numbers
            copy = nums[i + 1]
            nums[i + 1] = nums[i]
            nums[i] = copy

            # Iterate backwards to make sure there are no numbers before i greater than nums[i]
            k = i
            while k > 0:
                if nums[k] < nums[k - 1]:
                    copy = nums[k]
                    nums[k - 1] = nums[k]
                    nums[k] = copy
                k -= 1
            i += 1
    return nums
