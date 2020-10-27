# Given an array nums. We define a runing sum of an array as runningSum[i] = sum(nums[0]...nums[i]). Return the running sum of nums.

def runningSum(nums):
    sum=nums[0]
    for i in range(1,len(nums)):
        sum=sum+nums[i]
        nums[i]=sum
    return sum