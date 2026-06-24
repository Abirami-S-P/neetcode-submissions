class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ex = []
        for i in nums:
            if i in ex:
                return True
            ex.append(i)
        return False
        