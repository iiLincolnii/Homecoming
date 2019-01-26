nums.sort()
        for i in range(len(nums)):
            if len(nums) == 1:
                return nums[0]
            if nums[0] == nums[1]:
                del nums[0]
                del nums[0]
            else:
                return nums[0]
