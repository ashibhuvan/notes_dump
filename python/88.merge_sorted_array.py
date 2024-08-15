class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        '''
        1. create 3 pointers, 1 at n-1, one at m-1, and one at (n + m) - 1 or the last element in nums1
        2. Compare the values at n pointer and m pointer, which ever element is greater will be the element we put at nums1 end pointer
        3. if the element is in nums1 array, swap it and decrease the nums 1 pointer and the nums1 end pointer
        4. if the element is in num2a array, simply replace it and decrement nums2 pointer and zero pointer
        5. continue until we have used all the elements in nums2


        '''
        if n == 0:
            return

        if len(nums1) == 1:
            nums1[0] = nums2[0]
            return

        nums1_p = m  - 1
        nums1_z_p = (n + m) - 1
        nums2_p = n - 1

        while nums2_p > -1:
            
            # Find the greatest elem
            if nums1_p < 0 or nums2[nums2_p] >= nums1[nums1_p]:
                nums1[nums1_z_p] = nums2[nums2_p]
                nums2_p -= 1
                nums1_z_p -= 1
            else:
                nums1[nums1_z_p] = nums1[nums1_p]
                nums1[nums1_p] = 0
                nums1_p -= 1
                nums1_z_p -= 1
