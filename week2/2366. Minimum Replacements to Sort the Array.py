class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]>nums[i+1]):
                step=int((nums[i]-1)/nums[i+1])
                # print(step)
                count+=step
                nums[i]=int(nums[i]/(step+1))
        return count

