nums=[213,54,0,52,23,0,645,3]
def moveZeroes(nums):
    i, j = 0, 0
    while i < len(nums):
        if nums[i] == 0:
            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                j += 1
            if j >= len(nums):
                break
        i += 1
    print(nums)

moveZeroes(nums)
