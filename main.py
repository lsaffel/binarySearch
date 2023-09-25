class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while True:
            # find midpoint index in the array
            # mid = (left + right)//2  # integer division. Rounds down

            # the line above works, but this next line makes sure that it never
            # overflows, in case left and right are really large:
            mid = left + ((right - left) // 2)
            
            if nums[mid] == target:
                return mid
            if left == right:
                return -1
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid +1
            if mid < 0 or mid == len(nums):  # the midpoint index would be out of bounds of the array
                return -1
