class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        #print(nums)
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            twoSumResult = self.twoSum(nums, i)
            if twoSumResult is not None and len(twoSumResult) > 0:
                for j in twoSumResult:
                    res.add(tuple(j))

        return res
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        res = []
        p1 = k + 1
        p2 = len(nums) - 1
        target = -1 * nums[k]

        if p1 == k:
            p1 = 1
        if p2 == k:
            return None

        while p1 < p2 and p1 > k and p2 > k:
            sum = nums[p1] + nums[p2]
            if sum == target:
                j = [nums[p1], nums[k], nums[p2]]
                res.append(sorted(j))
                p1 += 1
                p2 -= 1
            
            if sum > target:
                p2 -= 1
                if p2 == k:
                    p2 -= 1
            if sum < target:
                p1 += 1
                if p1 == k:
                    p1 += 1
        return res
            
