# Find the First True in a Sorted Boolean Array
'''
An array of booleans is divided into two sections. The left section consists of all false and the right section consists of all true.
Find the First True in a Sorted Boolean Array of the right section. The index of the first true element. If there is no true element return -1

Input = [false, false, true, true, true]

Brute Force: Loop until you find the first true
Optimal: Use binary search
'''
def find_boundry(arr: List[int]) -> int:
    if not arr:
        return -1

    l,r = 0, len(arr) - 1
    boundary = -1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid]:
            boundary = mid
            r = mid - 1
        else:
            l = mid + 1
    return boundary
