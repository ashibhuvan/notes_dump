class Solution:

    def mergeSort(self, nums: List[int]) -> List[int]:

        # Return nums when size is 1  
        n = len(nums)
        if n <= 1:
            return nums
        # Split the array
        # Normally we would substract 1 to get the true index but due to the way I am splicing the list its not needed
        midIndex = (n // 2) 
        array1 = self.mergeSort(nums[:midIndex])
        array2 = self.mergeSort(nums[midIndex:])
        # Merge the 2 lists
        p1,p2 = 0,0
        sorted = []
        while p1 < len(array1) and p2 < len(array2):
            
            if array1[p1] <= array2[p2]:
                sorted.append(array1[p1])
                p1 += 1
            else 
                sorted.append(array2[p2])
                p2 += 1
        
        if p1 < len(array1):
            sorted.extend(array1[p1:])
        if p2 < len(array2):
            sorted.extend(array2[p2:])
        return sorted




