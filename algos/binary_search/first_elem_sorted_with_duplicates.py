'''
Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index.
Return -1 if the target is not in the array

'''
def find_first_occurrence(arr:List[int], target:int) -> int:
    l,r = 0, len(arr) - 1
    first_index = -1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            first_index = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return first_index
