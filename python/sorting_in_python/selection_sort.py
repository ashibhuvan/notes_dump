class SelectionSort:

    def sort(self, nums: List[int]) -> List[int]:

        n = len(nums)
        for i in range(n):

            minIndex = i

            for j in range(i, n):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]

        return nums
'''
Algorithim:
    Iterate through the array.
    On each iteration, look through the rest of the array if there is a smaller element
    Swap the element with the current index of iteration

Time Complexity:
    O(n) + O(n - 1) + O(n - 2) + ... = O(n ^ 2)
    Algorithim is not stable because an earlier element can jump after an element of the same value during swap
    Algorithim is in place as only additional memory is the storage of minIndex on each element

'''
