'''
Given ana rray of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target.
Assume that it is guaranteed to find a satisfying number

'''
def first_not_smaller(arr: List[int], target: int) -> int:
    l,r = 0, len(arr) - 1
    first_not_smaller = -1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            first_not_smaller = mid
            right = mid - 1
        else:
            left = mid + 1
    return first_not_smaller
