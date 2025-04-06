from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # Divide
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # Conquer (merge two sorted arrays)
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0
        
        # Merge step
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Append remaining
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged